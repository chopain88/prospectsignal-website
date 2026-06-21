#!/usr/bin/env python3
"""Regenerate sitemap.xml from the ACTUAL files in the repo. No hand-editing -> no 404 sitemap.
Run from repo root. Lists only pages that really exist."""
import json, os, glob, datetime
BASE="https://prospectsignal.com.au"
def mtime(p):
    try: return datetime.date.fromtimestamp(os.path.getmtime(p)).isoformat()
    except: return datetime.date.today().isoformat()
urls=[]
def add(loc, path, freq, pri):
    urls.append(f'  <url><loc>{BASE}{loc}</loc><lastmod>{mtime(path)}</lastmod><changefreq>{freq}</changefreq><priority>{pri}</priority></url>')
# core pages
core={"index.html":("/","weekly","1.0"),"mining.html":("/mining","weekly","0.9"),"mining-map.html":("/mining-map","monthly","0.6"),
 "transport.html":("/transport","weekly","0.9"),"products.html":("/products","weekly","0.8"),
 "faq.html":("/faq","monthly","0.8"),"methodology.html":("/methodology","monthly","0.5"),
 "responsible-use.html":("/responsible-use","monthly","0.4")}
for f,(loc,fr,pr) in core.items():
    if os.path.exists(f): add(loc,f,fr,pr)
# blog index + posts
if os.path.exists("blog/index.html"): add("/blog/","blog/index.html","weekly","0.7")
for f in sorted(glob.glob("blog/*.html")):
    s=os.path.basename(f)[:-5]
    if s=="index": continue
    add(f"/blog/{s}",f,"monthly","0.7")
# product pages (canonical set from products.json, only if the page exists)
prods=json.load(open("data/products.json"))
n=0
for p in prods:
    slug=p["slug"]; pf=f"product/{slug}.html"
    if os.path.exists(pf): add(f"/product/{slug}",pf,"monthly","0.6"); n+=1
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join(urls)+"\n</urlset>\n"
open("sitemap.xml","w").write(xml)
print(f"sitemap.xml regenerated: {len(urls)} URLs ({n} product pages)")
