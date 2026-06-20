#!/bin/bash
# One command: regenerate sitemap from live files -> commit/push (Netlify deploys) -> notify IndexNow
cd /mnt/homedata/ProspectSignalAU/repo
python3 generate_sitemap.py
git add -A && (git commit -m "SEO: auto-regenerate sitemap + notify search engines" || echo "no changes")
git push origin main
sleep 25
python3 ping_indexnow.py
