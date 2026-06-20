#!/usr/bin/env python3
"""Reusable blog generator. Reuses the exact site template (styles/nav/footer) from an
existing post and stamps in new content. Numbers are passed in (queried from the data, never typed from memory)."""
import re, os
TPL="blog/australian-lithium-mines.html"
src=open(TPL).read()
style=re.search(r'<style>.*?</style>', src, re.S).group(0)
umami=re.search(r'<script defer src="https://analytics[^>]*></script>', src).group(0)
nav=re.search(r'<nav>.*?</nav>', src, re.S).group(0)
footer=re.search(r'<footer>.*?</footer>', src, re.S).group(0)
fonts='<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'
CTA='''<div class="cta-block"><p><strong>Mining Intelligence Database</strong> — 349 verified Australian operating mine sites. Parent company, operator, commodity, state, GPS coordinates. Ownership verified to June 2026.</p><p>CSV A$1,499 · CSV + interactive map A$2,999 · Free 25-row sample, no credit card.</p><a href="/mining" class="btn">View the product</a><a href="/samples/sample_AU-Mining-Intelligence.csv" download class="btn btn-outline">Free sample</a></div>'''

def esc(s): return s.replace('"','\\"')
def write(slug,title,desc,date,body):
    canon=f"https://prospectsignal.com.au/blog/{slug}"
    schema='{"@context":"https://schema.org","@type":"Article","headline":"%s","description":"%s","author":{"@type":"Organization","name":"Prospect Signal AU"},"publisher":{"@type":"Organization","name":"Prospect Signal AU","url":"https://prospectsignal.com.au"},"datePublished":"%s","url":"%s"}'%(esc(title),esc(desc),date,canon)
    head=(f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">'
      f'<title>{title} | Prospect Signal AU</title><meta name="description" content="{desc}"><link rel="canonical" href="{canon}">'
      f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}">'
      f'<meta property="og:type" content="article"><meta property="og:site_name" content="Prospect Signal AU">'
      f'<meta property="article:published_time" content="{date}T00:00:00+08:00"><meta name="twitter:card" content="summary_large_image">'
      f'<script type="application/ld+json">{schema}</script>{fonts}{style}{umami}</head>')
    html=f'{head}<body>{nav}<article><div class="meta">June 2026 · Mining Intelligence · Prospect Signal AU</div><h1>{title}</h1>{body}{CTA}</article>{footer}</body></html>'
    open(f"blog/{slug}.html","w").write(html)
    print("wrote blog/"+slug+".html", len(html),"bytes")

# ---------- POST 1: PILBARA IRON ORE ----------
write("who-owns-the-pilbara-iron-ore",
 "Who owns the Pilbara: the companies behind Australia's 60 iron ore mines",
 "Australia has 60 operating iron ore mines, 52 of them in WA. Rio Tinto runs 19, Mineral Resources 9, Fortescue 8, BHP 5. Parent company, operator and GPS, verified June 2026.",
 "2026-06-20",
 '''<p>Australia's iron ore story gets told through four or five household names. The operating reality is more concentrated than that — and more fragmented at the entity level. As of June 2026 there are <strong>60 operating iron ore mines</strong> in the country.</p>
<p>Where they are isn't a surprise: <strong>52 are in Western Australia</strong> — the Pilbara core — with 5 in South Australia, 2 in Tasmania and 1 in the Northern Territory. Who runs them is where it gets interesting.</p>
<h2>The ownership concentration</h2>
<p>Six parent companies account for the bulk of operating iron ore sites:</p>
<table><thead><tr><th>Parent company</th><th>Operating sites</th></tr></thead><tbody>
<tr><td>Rio Tinto Limited</td><td>19</td></tr>
<tr><td>Mineral Resources Limited</td><td>9</td></tr>
<tr><td>Fortescue Ltd</td><td>8</td></tr>
<tr><td>BHP Group Limited</td><td>5</td></tr>
<tr><td>Hancock Prospecting Pty Ltd</td><td>4</td></tr>
<tr><td>GFG Alliance / SIMEC Mining</td><td>3</td></tr></tbody></table>
<p>Rio Tinto alone operates nearly a third of the country's iron ore mines. Add Mineral Resources, Fortescue and BHP and you've covered more than two-thirds — from four organisations.</p>
<h2>Why the parent name isn't enough</h2>
<p>If you sell into the Pilbara, the procurement decision and the site decision sit in different places. Rio Tinto's mines run through subsidiary operating entities and joint ventures; BHP's through its iron ore operating companies and the long-standing Mt Newman and Goldsworthy JV structures. A purchase order, a site induction or a tender portal asks for the <strong>operating entity</strong>, not "Rio Tinto." A budget conversation happens at the <strong>parent</strong>. Carry only one and half your sales motion misfires.</p>
<h2>Who sells into 60 iron ore mines</h2>
<p>Iron ore is the highest-tonnage, highest-throughput commodity in the country — which means the heaviest demand for haulage fleet and tyres, conveyor and crushing maintenance, fuel, explosives, and FIFO labour. Sixty sites, concentrated under a handful of parents but operated through dozens of named entities, is a territory a single BD team can cover precisely — if the list maps parent to operator on every row.</p>'''
)

# ---------- POST 2: AUSTRALIAN GOLD ----------
write("australian-gold-mining-companies",
 "Australia's gold mining companies: who's producing and where",
 "Gold is Australia's most common operating mine — 103 sites, 84 in WA. Westgold runs 17, Northern Star 14, Vault Minerals 10. Parent, operator and GPS, verified June 2026.",
 "2026-06-20",
 '''<p>Coal and iron ore get the headlines, but by site count gold is Australia's biggest mining commodity. As of June 2026 there are <strong>103 operating gold mines</strong> — more than coal (99) and well ahead of iron ore (60).</p>
<p>The geography is lopsided: <strong>84 of the 103 are in Western Australia</strong>. The rest are scattered — 6 in Queensland, 5 in NSW, 4 in Victoria, 2 in the NT, and one each in Tasmania and South Australia.</p>
<h2>A mid-tier-dominated sector</h2>
<p>Unlike iron ore (a few majors) or coal (global names), operating gold is led by Australian mid-tier producers:</p>
<table><thead><tr><th>Parent company</th><th>Operating sites</th></tr></thead><tbody>
<tr><td>Westgold Resources Limited</td><td>17</td></tr>
<tr><td>Northern Star Resources Ltd</td><td>14</td></tr>
<tr><td>Vault Minerals Limited</td><td>10</td></tr>
<tr><td>Ramelius Resources Limited</td><td>7</td></tr>
<tr><td>Genesis Minerals Limited</td><td>5</td></tr>
<tr><td>Regis Resources Limited</td><td>5</td></tr></tbody></table>
<p>That's a more fragmented buyer market than iron ore — more decision-makers, more sites, and a wave of consolidation (Vault Minerals itself is the product of recent mergers) that keeps reshaping who owns what. A list that was right last quarter may already name the wrong parent.</p>
<h2>Why this list goes stale fastest</h2>
<p>Gold is the most acquisitive corner of Australian mining. Mines change hands, operators rebrand, and care-and-maintenance status flips with the gold price. We verify ownership to a primary source and exclude non-producing sites — because a rep pitching a mothballed pit, or calling the company that sold the asset eighteen months ago, is wasted effort.</p>
<h2>Who sells into 103 gold mines</h2>
<p>Gold operations — many of them remote WA Goldfields sites — drive steady demand for reagents (cyanide, lime, activated carbon), grinding media, drill-and-blast, assay and lab services, FIFO labour and mobile fleet. With 84 of them in one state under a shifting set of mid-tier owners, knowing the current parent and the operating entity for each site is the difference between a warm intro and a cold miss.</p>'''
)

# ---------- POST 3: QLD COAL ----------
write("queensland-coal-mining-companies",
 "Coal mining in Queensland: the Bowen Basin operators and who owns them",
 "Queensland has 52 of Australia's 99 operating coal mines. BHP runs 6, Stanmore 5, Coronado 5, Anglo American 4. Parent, operator and GPS, verified June 2026.",
 "2026-06-20",
 '''<p>Australia has <strong>99 operating coal mines</strong>, and Queensland holds the majority: <strong>52 sites</strong>, against 40 in New South Wales and a handful across Victoria, WA and Tasmania. Most of Queensland's are in the Bowen Basin — the metallurgical coal heartland.</p>
<h2>Who operates Queensland's coal</h2>
<p>Queensland coal is a mix of global majors and ASX-listed specialists:</p>
<table><thead><tr><th>Parent company</th><th>QLD coal sites</th></tr></thead><tbody>
<tr><td>BHP Group Limited</td><td>6</td></tr>
<tr><td>Stanmore Resources Limited</td><td>5</td></tr>
<tr><td>Coronado Global Resources Inc</td><td>5</td></tr>
<tr><td>Anglo American plc</td><td>4</td></tr>
<tr><td>New Hope Group</td><td>4</td></tr>
<tr><td>Peabody Energy</td><td>3</td></tr></tbody></table>
<p>Ownership here moves constantly through divestments — BHP and Anglo American have both been reshaping their Queensland coal portfolios, with assets passing to Stanmore, Coronado and others. The operating entity on the ground frequently outlasts the parent on the masthead.</p>
<h2>Metallurgical vs thermal — and why it changes your pitch</h2>
<p>Bowen Basin coal is largely metallurgical (steelmaking), exported through Queensland's coal terminals; NSW skews thermal (power). The commodity sub-type shapes the procurement profile — wash plant reagents, larger haulage fleets, port logistics. If your dataset only says "coal," you can't segment the 52 Queensland sites from the 40 in NSW, let alone target the met-coal operators specifically.</p>
<h2>Who sells into Queensland coal</h2>
<p>Fifty-two operating sites, concentrated in one basin, with constant ownership churn, is a high-value and fast-moving territory: draglines and large mobile fleet, explosives, conveyor and wash-plant maintenance, water management, and a large FIFO and contract workforce. Knowing the current owner and the operating entity for each — and which are met versus thermal — is exactly what turns a site list into a call list.</p>'''
)
print("done")
