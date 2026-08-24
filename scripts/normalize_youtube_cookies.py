"""Normalize common browser cookie exports to yt-dlp's Netscape format."""

import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, Iterable


def _cookie_items(data: Any) -> Iterable[Dict[str, Any]]:
    if isinstance(data, list):
        return (item for item in data if isinstance(item, dict))
    if isinstance(data, dict):
        for key in ("cookies", "items", "entries"):
            value = data.get(key)
            if isinstance(value, list):
                return (item for item in value if isinstance(item, dict))
    return ()


def _expiry(cookie: Dict[str, Any]) -> str:
    value = cookie.get("expirationDate", cookie.get("expires", cookie.get("expiration", 0)))
    try:
        number = float(value or 0)
    except (TypeError, ValueError):
        number = 0
    if not math.isfinite(number) or number <= 0:
        return "0"
    return str(int(number))


def normalize(path: Path) -> str:
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    first_line = next((line.strip() for line in raw.splitlines() if line.strip()), "")
    if first_line.startswith("# Netscape HTTP Cookie File") or first_line.startswith("# HTTP Cookie File"):
        return "netscape"

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return "unsupported"

    lines = ["# Netscape HTTP Cookie File", "# This file was normalized on the ephemeral GitHub Actions runner."]
    converted = 0
    for cookie in _cookie_items(data):
        domain = str(cookie.get("domain") or cookie.get("host") or "").strip()
        name = str(cookie.get("name") or "").strip()
        if not domain or not name:
            continue
        host_only = bool(cookie.get("hostOnly", False))
        include_subdomains = "FALSE" if host_only and not domain.startswith(".") else "TRUE"
        if include_subdomains == "TRUE" and not domain.startswith("."):
            domain = "." + domain
        if bool(cookie.get("httpOnly", False)) and not domain.startswith("#HttpOnly_"):
            domain = "#HttpOnly_" + domain
        cookie_path = str(cookie.get("path") or "/")
        secure = "TRUE" if bool(cookie.get("secure", False)) else "FALSE"
        value = str(cookie.get("value") or "")
        lines.append("\t".join((domain, include_subdomains, cookie_path, secure, _expiry(cookie), name, value)))
        converted += 1

    if not converted:
        return "unsupported"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return f"converted-json:{converted}"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: normalize_youtube_cookies.py PATH", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.exists() or path.stat().st_size == 0:
        print("missing-or-empty")
        return 0
    print(normalize(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
