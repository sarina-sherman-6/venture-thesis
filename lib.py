import json, html
from data import COMPANIES, DEALS, slug

E = html.escape
UPDATED = "October 12, 2026"
THESES = [
 ("fiber","Fiber","fiber.html","#6F7F2E"),
 ("nonalc","Non-Alc","non-alc.html","#EF5B2B"),
 ("meat","Meat Protein","meat-protein.html","#7A2E3B"),
 ("wear","Wearables","wearables.html","#9B72CF"),
]
# dropdown entries per thesis page: (anchor, label)
MENUS = {
 "fiber": [("summary","The case in 60 seconds"),("science","The science"),("types","Fiber types"),("rules","Regulation"),("market","Market size"),("outlook","Growth outlook"),("deals","Deal flow"),("landscape","Company landscape"),("funds","Active investors"),("strategics","Strategic activity"),("voices","Notable voices"),("thesis","Investment thesis"),("risks","Key risks"),("sources","Sources")],
}
STD = [("summary","The case in 60 seconds"),("context","Why now"),("segments","Category map"),("rules","Regulation"),("outlook","Market and outlook"),("deals","Deal flow"),("landscape","Company landscape"),("funds","Active investors"),("strategics","Strategic activity"),("voices","Notable voices"),("thesis","Investment thesis"),("risks","Key risks"),("sources","Sources")]
for k in ("nonalc","meat","wear"): MENUS[k] = STD

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
FAVICON = "<link rel=\"icon\" href=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='16' fill='%23EF5B2B'/%3E%3Ctext x='16' y='22' text-anchor='middle' font-family='Arial' font-weight='bold' font-size='17' fill='%23FBF8EF'%3ES%3C/text%3E%3C/svg%3E\">"

def nav(current):
    items = []
    for k, name, page, col in THESES:
        cur = ' aria-current="page"' if current == k else ''
        links = ''.join(f'<li><a href="{page}#{a}">{E(l)}</a></li>' for a, l in MENUS[k])
        items.append(f'<li><a class="top" data-dd href="{page}"{cur}><i class="dot" style="background:{col}"></i>{name}<i class="chev"></i></a><ul class="menu"><li><span class="mhead">{name} thesis</span></li>{links}</ul></li>')
    cur = ' aria-current="page"' if current == "db" else ''
    n_co = len(COMPANIES)
    items.append(f'<li><a class="top dbtab" href="companies.html"{cur}><svg viewBox="0 0 16 16" aria-hidden="true"><ellipse cx="8" cy="3.5" rx="6" ry="2.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M2 3.5v9c0 1.2 2.7 2.2 6 2.2s6-1 6-2.2v-9M2 8c0 1.2 2.7 2.2 6 2.2s6-1 6-2.2" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>Company database<span class="cnt">{n_co}</span></a></li>')
    mob = ''.join(f'<details><summary><i class="dot" style="background:{col}"></i>{name}</summary><a href="{page}">Overview</a>' + ''.join(f'<a href="{page}#{a}">{E(l)}</a>' for a, l in MENUS[k]) + '</details>' for k, name, page, col in THESES)
    return f'''<nav class="bar" aria-label="Site">
  <div class="wrap">
    <a class="brand" href="./"><span class="mark">S</span><b>Sarina's Venture Thesis</b></a>
    <ul class="nav">{''.join(items)}</ul>
    <a class="navcta" href="./#about">Contact</a>
    <button class="navtoggle" id="navToggle" aria-expanded="false" aria-controls="mpanel">Menu</button>
  </div>
  <div class="wrap mpanel" id="mpanel" hidden><a href="./">Home</a>{mob}<a class="mdb" href="companies.html">Company database ({len(COMPANIES)} companies)</a><a href="./#about">Contact</a></div>
</nav>'''

FOOT = f'''<footer><div class="wrap">
  <div class="fgrid">
    <div><b>Sarina's Venture Thesis</b><p>Independent research on four consumer theses: fiber, non-alc, the return of meat protein, and discreet wearables for women's health.</p></div>
    <div><p><strong style="color:#F9D8C6">Author</strong></p><p>Sarina Sherman<br>MBA Candidate, Columbia Business School</p><p>ssherman28@gsb.columbia.edu<br>(312) 965-9951</p><p><a href="https://www.linkedin.com/in/sarina-sherman/" target="_blank" rel="noopener">LinkedIn</a> &nbsp;&middot;&nbsp; <a href="https://substack.com/@sarinasherman" target="_blank" rel="noopener">Substack</a> &nbsp;&middot;&nbsp; <a href="https://sarina-sherman-6.github.io/CBS-MBA-AI-Portfolio/" target="_blank" rel="noopener">Portfolio</a></p></div>
    <div><p><strong style="color:#F9D8C6">Methodology</strong></p><p>Company and deal data come from press releases, filings, and trade press, reviewed weekly. Market estimates are third-party and vary by methodology. Landscape placements are the author's judgment.</p></div>
  </div>
  <div class="fine">&copy; 2026 Sarina Sherman. Updated {UPDATED}. For informational purposes only; not investment advice.</div>
</div></footer>'''

def page(title, desc, current, body, charts=None, companies=False, artifact=False, main=False):
    """artifact+main -> no doctype/html/head/body wrapper"""
    head = f'<title>{E(title)}</title>\n<meta name="description" content="{E(desc)}">\n<meta property="og:title" content="{E(title)}">\n<meta property="og:description" content="{E(desc)}">\n{FAVICON}\n{FONTS}\n<link rel="stylesheet" href="assets/site.css">'
    scripts = ''
    if companies: scripts += '<script src="assets/companies.js"></script>'
    scripts += f'<script>window.CHARTS={json.dumps(charts or [], ensure_ascii=False)};</script><script src="assets/site.js"></script>'
    inner = f'{nav(current)}\n<main id="top">\n{body}\n</main>\n{FOOT}\n{scripts}'
    if artifact and main:
        return head + '\n' + inner
    return f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n{head}\n</head>\n<body>\n{inner}\n</body>\n</html>\n'

# ---------- section helpers ----------
def section(id, h2, lede, inner, cls=''):
    l = f'<p class="lede">{lede}</p>' if lede else ''
    c = f' class="{cls}"' if cls else ''
    return f'<section id="{id}"{c}>\n<div class="wrap">\n  <h2>{h2}</h2>\n  {l}\n{inner}\n</div>\n</section>\n'

def cards(items, cls='cards', strat=False):
    return f'<div class="{cls}">' + ''.join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in items) + '</div>'

def voices(items):
    out = []
    for q, name, role, contra in items:
        out.append(f'<figure class="voice{" contra" if contra else ""}"><blockquote>{q}</blockquote><figcaption><strong>{name}</strong>{role}</figcaption></figure>')
    return '<div class="voices">' + ''.join(out) + '</div>'

def table(headers, rows, minw=640, fg=None, tags=None):
    a = f' data-fg="{fg}"' if fg else ''
    th = ''.join(f'<th>{h}</th>' for h in headers)
    trs = []
    for i, r in enumerate(rows):
        t = f' data-tags="{tags[i]}"' if tags else ''
        trs.append(f'<tr{t}>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>')
    return f'<div class="tbl"><table style="min-width:{minw}px"{a}><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>'

def figure(id, h3, cap, legend='', wide=False, extra=''):
    return f'<figure class="chart{" wide" if wide else ""}"><figcaption><h3>{h3}</h3><p>{cap}</p></figcaption><div id="{id}" class="chartbox"></div>{legend}{extra}</figure>'

def legend(items):
    return '<div class="legend">' + ''.join(f'<span><i style="background:{c}{";border:1px solid #5B3E86" if b else ""}"></i>{t}</span>' for c, t, b in items) + '</div>'

def hero(thesis, eyebrow, h1, sub, picks, facts, col):
    ops = ''.join(f'<li><a class="opp" href="companies.html#co-{slug(n)}"><span class="rk">{i+1}</span><span class="ob"><strong>{E(n)}</strong><span class="tag">{t}</span><em>{w}</em></span></a></li>' for i, (n, t, w) in enumerate(picks))
    fs = ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in facts)
    return f'''<div class="wrap">
<header class="hero">
  <div>
    <span class="eyebrow"><i style="background:{col}"></i>{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
    <p class="meta"><span>By Sarina Sherman, Columbia Business School</span><span class="sep"></span><span>Updated {UPDATED}</span><span class="sep"></span><span>Refreshed weekly</span></p>
    <div class="ctas"><a class="p" href="#landscape">See the company landscape</a><a class="s" href="#thesis">Read the investment thesis</a></div>
  </div>
  <aside class="topops" aria-labelledby="topopsT">
    <div class="topops-head"><h2 id="topopsT">Top VC opportunities</h2><a href="companies.html#t-{thesis}" class="seeall">All {E(dict((k,n) for k,n,_,_ in THESES)[thesis])} companies</a></div>
    <ol>{ops}</ol>
    <p class="topops-note">Author's picks. Select a company to open its profile in the database.</p>
  </aside>
</header>
<div class="facts">{fs}</div>
</div>
'''

def summary(items):
    cs = ''.join(f'<a class="sumcard" href="#{a}"><span class="sumk">{k}</span><h3>{h}</h3><p>{p}</p><span class="go">{g}</span></a>' for k, h, p, a, g in items)
    return section("summary", "The case in 60 seconds", None, f'<div class="sumgrid">{cs}</div>', 'summary')

def deals_section(thesis, lede, extra_figs='', extra_charts=None):
    D = DEALS[thesis]
    rows, tags = [], []
    for key, lab, co, sub, deal, backers, read, kind, m in D:
        rows.append([lab, f'<strong>{E(co)}</strong><span class="sub">{E(sub)}</span>', E(deal), E(backers), E(read)])
        tags.append({'r':'raise','e':'exit','s':'strategic'}[kind])
    ctl = '<div class="controls" role="group" aria-label="Filter deals"><button class="flt" data-g="deals" data-f="all" aria-pressed="true">All</button><button class="flt" data-g="deals" data-f="raise" aria-pressed="false">Venture raises</button><button class="flt" data-g="deals" data-f="exit" aria-pressed="false">Exits and IPOs</button><button class="flt" data-g="deals" data-f="strategic" aria-pressed="false">Strategic moves</button></div>'
    tl = [[co, key, m, kind, lab] for key, lab, co, sub, deal, backers, read, kind, m in D if m]
    figs = figure("chTimeline", "Disclosed deal sizes over time", "Each disclosed raise or exit by date and size, on a log scale so small and large deals fit together.", legend([("#1C1B1F","Venture raise",0),("#EF5B2B","Exit, acquisition, or IPO",0)]), wide=True)
    if len(tl) < 3: figs = ''
    grid = f'<div class="chartgrid">{figs}{extra_figs}</div>' if (figs or extra_figs) else ''
    inner = f'{grid}{ctl}' + table(["When","Company","Deal","Backers or buyer","Read-through"], rows, 860, fg="deals", tags=tags)
    charts = ([{"type":"timeline","id":"chTimeline","deals":tl}] if len(tl) >= 3 else []) + (extra_charts or [])
    return section("deals", "Deal flow", lede, inner), charts

def landscape_section(name, points, note=''):
    pts = [[p[0], p[1], p[2], p[3], p[4], p[5], slug(p[0])] for p in points]
    fig = figure("chLand", f"{name}: leaders vs. untapped opportunities", "Scale today (capital, distribution, brand reach) against room for upside for an early-stage investor. Dot size reflects disclosed capital. Author's assessment; select a company to open its profile.",
                 legend([("#1C1B1F","On the watch list",0),("#EF5B2B","Acquired or exited",0),("#BDB6AE","Scaled or incumbent",0),("#EBDDF8","Early, not yet on watch list",1),("#FFFFFF","Declining",1)]), wide=True)
    inner = f'<div class="chartgrid">{fig}</div>' + (f'<p class="note mt">{note}</p>' if note else '') + f'<p class="mt"><a href="companies.html">Open the full company database</a>, which spans all four theses with filters, sorting, and search.</p>'
    return section("landscape", "Company landscape", None, inner), {"type":"quadrant","id":"chLand","points":pts,"click":True,"xl":"Scale today: capital, distribution, brand reach →","xs":"Scale today →","yl":"Room for upside for an early investor →","ys":"Upside →"}

def thesis_section(statement, plays, look, outside, opp):
    inner = f'<div class="thesis-box"><p>{statement}</p></div>' + cards(plays, 'plays') + \
        f'<div class="two"><div><h3>Investment criteria</h3><ul class="chips">{"".join(f"<li>{x}</li>" for x in look)}</ul></div><div class="dark"><h3>Outside the thesis</h3><ul>{"".join(f"<li>{x}</li>" for x in outside)}</ul></div></div>' + \
        f'<div class="callout mt"><h3>Open opportunities</h3><p>{opp}</p></div>'
    return section("thesis", "Investment thesis", None, inner)

def risks_section(rows):
    return section("risks", "Key risks", None, table(["Risk","Evidence","How good companies mitigate it"], [[f"<strong>{a}</strong>", b, c] for a, b, c in rows], 640))

def sources_section(items):
    lis = ''.join(f'<li>{s}</li>' for s in items)
    return f'<section class="sources" id="sources"><div class="wrap"><h2 style="font-size:1.6rem;margin-bottom:20px">Sources</h2><ol>{lis}</ol></div></section>\n'

def src(pub, date, title, url):
    return f'{E(pub)}. ({E(date)}). <a href="{url}" target="_blank" rel="noopener">{E(title)}</a>.'

def pagenext(prev, nxt):
    def a(x, lab):
        if not x: return '<div></div>'
        k, n, p, c = x
        return f'<div><span>{lab}</span><a href="{p}">{n} thesis</a></div>'
    return f'<div class="wrap pagenext">{a(prev,"Previous")}{a(nxt,"Next")}</div>'
