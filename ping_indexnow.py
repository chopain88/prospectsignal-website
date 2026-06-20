#!/usr/bin/env python3
"""Notify IndexNow (Bing, Copilot, Yandex, Seznam) of all live URLs. Run after each deploy."""
import json, re, urllib.request
KEY="d0526918253ac9cc85e481233c101212"
HOST="prospectsignal.com.au"
urls=re.findall(r"<loc>(.*?)</loc>", open("sitemap.xml").read())
payload={"host":HOST,"key":KEY,"keyLocation":f"https://{HOST}/{KEY}.txt","urlList":urls}
req=urllib.request.Request("https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode(), headers={"Content-Type":"application/json; charset=utf-8"}, method="POST")
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow: HTTP {r.status} for {len(urls)} URLs")
except urllib.error.HTTPError as e:
    print(f"IndexNow: HTTP {e.code} for {len(urls)} URLs ({e.reason})")
