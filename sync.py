"""Copy selected public M3U playlists into this repository."""

import json
import os
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
DEST = ROOT / "m3u"
LIMIT = 20 * 1024 * 1024


def download(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "M3U-Mirror/1.0"})
    with urlopen(request, timeout=30) as response:
        data = response.read(LIMIT + 1)
    if len(data) > LIMIT:
        raise ValueError("playlist exceeds 20 MiB")
    if not data.lstrip(b"\xef\xbb\xbf \t\r\n").startswith(b"#EXTM3U"):
        raise ValueError("response is not an extended M3U playlist")
    return data


def main() -> None:
    DEST.mkdir(exist_ok=True)
    sources = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    wanted = {source["file"] for source in sources}
    failures = []
    for source in sources:
        filename = source["file"]
        if Path(filename).name != filename or not filename.endswith(".m3u"):
            raise ValueError(f"invalid destination filename: {filename}")
        target = DEST / filename
        try:
            data = download(source["url"])
            if not target.exists() or target.read_bytes() != data:
                temporary = target.with_suffix(".m3u.tmp")
                temporary.write_bytes(data)
                os.replace(temporary, target)
                print(f"updated {filename}: {len(data)} bytes")
            else:
                print(f"unchanged {filename}")
        except Exception as exc:
            failures.append(f"{filename}: {exc}")
            print(f"failed {filename}: {exc}")
    if failures:
        raise SystemExit("\n".join(failures))
    for stale in DEST.glob("*.m3u"):
        if stale.name not in wanted:
            stale.unlink()
            print(f"removed excluded file {stale.name}")


if __name__ == "__main__":
    main()
