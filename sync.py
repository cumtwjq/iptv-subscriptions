"""Copy selected public M3U playlists into this repository."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
DEST = ROOT / "m3u"
LIMIT = 20 * 1024 * 1024
GENERAL_LIST = "aptv-iptv.m3u"
EPG_URLS = (
    "https://epg.zsdc.eu.org/t.xml",
    "http://epg.51zmt.top:8000/e.xml.gz",
)
EPG_ATTRIBUTE_RE = re.compile(r'\s(x-tvg-url|url-tvg|tvg-url)="[^"]*"')
EXTRA_SOURCES = (
    (
        "445569",
        "https://iptv.445569.xyz/live.m3u",
        {
            "🎞️电影直播": "电影",
            "📺电视剧直播": "电视剧",
            "🎎动漫直播": "动漫",
            "🤣沙雕动画直播": "动漫",
        },
    ),
    (
        "suxuang",
        "https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u",
        {
            "电视剧频道": "电视剧",
            "动画频道": "动漫",
            "虎牙影视": "电影",
            "斗鱼影视": "电影",
            "点播电影": "电影",
        },
    ),
)
GROUP_RE = re.compile(r'group-title="([^"]*)"')
REPLACEMENT_CHANNEL = (
    '#EXTINF:-1 tvg-logo="https://epg.112114.xyz/logo/%E4%B8%83%E9%BE%99%E7%8F%A0.png" '
    'group-title="动漫",七龙珠\n'
    'https://huyazhibo.de5.net/?id=10279885\n'
).encode("utf-8")


def download(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "M3U-Mirror/1.0"})
    with urlopen(request, timeout=30) as response:
        data = response.read(LIMIT + 1)
    if len(data) > LIMIT:
        raise ValueError("playlist exceeds 20 MiB")
    if not data.lstrip(b"\xef\xbb\xbf \t\r\n").startswith(b"#EXTM3U"):
        raise ValueError("response is not an extended M3U playlist")
    return data


def replace_epg(data: bytes) -> bytes:
    """Replace only the EPG header; preserve channel data and other options."""
    first_line, newline, rest = data.partition(b"\n")
    header = first_line.decode("utf-8-sig").rstrip("\r")
    if not header.startswith("#EXTM3U"):
        raise ValueError("missing M3U header")
    match = EPG_ATTRIBUTE_RE.search(header)
    attribute = match.group(1) if match else "x-tvg-url"
    other_options = EPG_ATTRIBUTE_RE.sub("", header)[len("#EXTM3U"):]
    replacement = f'#EXTM3U {attribute}="{",".join(EPG_URLS)}"{other_options}'
    ending = b"\r\n" if first_line.endswith(b"\r") else newline
    return replacement.encode("utf-8") + ending + rest


def selected_channels(data: bytes, groups: dict[str, str]) -> tuple[bytes, int]:
    """Keep playable entries in selected groups, including their playback options."""
    result = []
    count = 0
    entry = []
    selected = False

    def finish() -> None:
        nonlocal count
        if not selected or not entry:
            return
        # An entry can include commented-out old links before its live link.
        active = [line for line in entry[1:] if line and not line.startswith("#")]
        if not active:
            return
        result.append("\n".join([entry[0], *(
            line for line in entry[1:] if line.startswith(("#EXTVLCOPT", "#KODIPROP"))
        ), active[0]]))
        count += 1

    for line in data.decode("utf-8-sig").splitlines():
        line = line.strip()
        if line.startswith("#EXTINF"):
            finish()
            match = GROUP_RE.search(line)
            group = groups.get(match.group(1)) if match else None
            selected = group is not None and line.rsplit(",", 1)[-1].strip() != "七龙珠"
            entry = [GROUP_RE.sub(f'group-title="{group}"', line, count=1) if group else line]
        elif entry:
            entry.append(line)
    finish()
    return ("\n".join(result) + "\n").encode("utf-8") if result else b"", count


def merge_general(base: bytes, previous: bytes) -> bytes:
    """Refresh each extra independently; retain its last good copy on failure."""
    combined = base.rstrip(b"\r\n") + b"\n"
    for key, url, groups in EXTRA_SOURCES:
        start = f"# BEGIN EXTRA {key}\n".encode()
        end = f"# END EXTRA {key}\n".encode()
        try:
            extra, count = selected_channels(download(url), groups)
            if not extra:
                raise ValueError("no playable channels in selected groups")
            print(f"extra {key}: {count} channels")
        except Exception as exc:
            old_start = previous.find(start)
            old_end = previous.find(end, old_start + len(start)) if old_start >= 0 else -1
            if old_end < 0:
                print(f"extra {key}: unavailable ({exc}); no prior copy")
                continue
            extra, _ = selected_channels(
                previous[old_start + len(start):old_end],
                {"电影": "电影", "电视剧": "电视剧", "动漫": "动漫"},
            )
            print(f"extra {key}: unavailable ({exc}); retained prior copy")
        combined += start + extra + end
    first_anime = re.search(r'(?m)^#EXTINF:[^\r\n]*group-title="动漫"'.encode("utf-8"), combined)
    if first_anime:
        return combined[:first_anime.start()] + REPLACEMENT_CHANNEL + combined[first_anime.start():]
    return combined + REPLACEMENT_CHANNEL


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
            data = replace_epg(download(source["url"]))
            if filename == GENERAL_LIST:
                previous = target.read_bytes() if target.exists() else b""
                data = merge_general(data, previous)
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
