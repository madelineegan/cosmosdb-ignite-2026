#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href and href.startswith("https://"):
                self.links.append(href)


parser = LinkParser()
parser.feed(Path("index.html").read_text(encoding="utf-8"))
failed = []
for url in sorted(set(parser.links)):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 BRK367-link-check/1.0"})
    try:
        with urlopen(request, timeout=20) as response:
            status = response.status
            final = response.geturl()
        print(f"{status} {url} -> {final}")
        if status >= 400:
            failed.append(url)
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"FAIL {url}: {exc}")
        failed.append(url)

if failed:
    raise SystemExit(f"{len(failed)} link(s) failed")
