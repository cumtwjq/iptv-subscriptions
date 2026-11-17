"""Cache mirrored playlists from GitHub Pages and serve them on the LAN."""

import os
import json
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen


CACHE = Path("/data")
BASE = os.environ["PAGES_BASE"].rstrip("/")
INTERVAL = max(60, int(os.environ.get("REFRESH_SECONDS", "1800")))
LIMIT = 20 * 1024 * 1024

if not BASE.startswith("https://"):
    raise ValueError("set PAGES_BASE to your own GitHub Pages URL")


def refresh() -> None:
    try:
        request = Request(f"{BASE}/sources.json", headers={"User-Agent": "M3U-Mirror-NAS/1.0"})
        with urlopen(request, timeout=30) as response:
            sources = json.load(response)
        files = [source["file"] for source in sources]
        if not files or any(Path(name).name != name or not name.endswith(".m3u") for name in files):
            raise ValueError("invalid source list")
    except Exception as exc:
        print(f"source list update failed: {exc}; retaining cached files", flush=True)
        return
    for source in sources:
        name = source["file"]
        urls = [f"{BASE}/{quote(name)}", source["url"]]
        data = None
        for url in urls:
            try:
                request = Request(url, headers={"User-Agent": "M3U-Mirror-NAS/1.0"})
                with urlopen(request, timeout=30) as response:
                    candidate = response.read(LIMIT + 1)
                if len(candidate) > LIMIT or not candidate.lstrip(b"\xef\xbb\xbf \t\r\n").startswith(b"#EXTM3U"):
                    raise ValueError("invalid or oversized M3U response")
                data = candidate
                break
            except Exception as exc:
                print(f"download failed for {name} from {url}: {exc}", flush=True)
        if data is None:
            print(f"refresh failed for {name}; keeping last good copy", flush=True)
            continue
        try:
            target = CACHE / name
            if not target.exists() or target.read_bytes() != data:
                temporary = CACHE / f".{name}.tmp"
                temporary.write_bytes(data)
                os.replace(temporary, target)
            print(f"cached {name}: {len(data)} bytes", flush=True)
        except Exception as exc:
            print(f"refresh failed for {name}: {exc}; keeping last good copy", flush=True)


def refresh_loop() -> None:
    while True:
        refresh()
        time.sleep(INTERVAL)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(CACHE), **kwargs)

    def guess_type(self, path):
        if path.endswith(".m3u"):
            return "text/plain; charset=utf-8"
        return super().guess_type(path)


if __name__ == "__main__":
    CACHE.mkdir(parents=True, exist_ok=True)
    threading.Thread(target=refresh_loop, daemon=True).start()
    print("serving cached playlists on port 8098", flush=True)
    ThreadingHTTPServer(("0.0.0.0", 8098), Handler).serve_forever()
