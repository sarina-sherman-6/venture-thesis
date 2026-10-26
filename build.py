import re, json, os, shutil, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from lib import *
from data import COMPANIES, DEALS, slug
import pages_new

SRC = open(os.path.join(ROOT, 'source', 'fiber-index.html')).read()
COLMAP = {'#3E5E46':'#1C1B1F','#A8843A':'#EF5B2B','#9AA79B':'#BDB6AE','#C9D9C0':'#EBDDF8','#9AB58D':'#5B3E86','#E2EBDB':'#F4EDFB','#8FB27A':'#C9B1E8','#C9A24E':'#F2A07B'}
def recolor(h):
    for a, b in COLMAP.items(): h = h.replace(a, b)
    return h
def grab(id):
    m = re.search(r'<section[^>]*id="%s"[^>]*>.*?</section>' % id, SRC, re.S)
    return m.group(0)

# ======================= FIBER =======================
def fiber():
    col = '#6F7F2E'
    h = hero("fiber", "Thesis: fiber and gut health", "Fiber is the next protein",
        "Most Americans miss their fiber target while GLP-1 use, endurance training, and AI tracking make the gap visible. The winners make clinically credible fiber easy to take every day through formulation or ingredient IP, not grams alone.",
        [("Floura","Untapped","National Starbucks launch on only a few million raised. Founder built Jeni's."),
         ("Supergut","Breakout","Clinical study plus GLP-1 booster. A natural strategic target."),
         ("Myota","Ingredient IP","$4.5M Series A; clinically validated fiber blends entering U.S. B2B."),
         ("BelliWelli","Breakout","405% revenue growth; two years past its last round."),
         ("Bellway","Untapped","Clean-label Metamucil challenger, small relative to the category.")],
        [("15–30%","lower all-cause and cardiovascular mortality for the highest fiber eaters vs. the lowest"),("1 in 8","U.S. adults currently taking a GLP-1"),("$3.15B+","in fiber-adjacent exits since 2025 (Poppi, Grüns)"),("18","isolated or synthetic fibers the FDA lets brands count as dietary fiber")], col)
    sec = {k: recolor(grab(k)).replace('href="#database"', 'href="companies.html#t-fiber"') for k in ["summary","science","types","rules","market","outlook","funds","strategics","voices","thesis","risks","sources"]}
    sec["voices"] = sec["voices"].replace("<blockquote>Counterpoint: argues", "<blockquote>Argues")
    # rebuild fiber types table statically
    types = json.loads(re.search(r'var types=(\[.*?\]);\n', SRC, re.S).group(1))
    trs = ''.join(f'<tr data-tags="{" ".join(t[6])}"><td><strong>{E(t[0])}</strong></td><td>{E(t[1])}</td><td>{E(t[2])}</td><td>{E(t[3])}</td><td>{E(t[4])}</td><td>{E(t[5])}</td></tr>' for t in types)
    sec["types"] = sec["types"].replace('<tbody></tbody>', f'<tbody>{trs}</tbody>').replace('<table id="typesTbl">', '<table id="typesTbl" data-fg="types" style="min-width:860px">')
    # outlook: legend for size uses recolored values already
    deals, dch = deals_section("fiber", "Raises, exits, and strategic deals that set the comps for the category, newest first.",
        extra_figs=figure("chMultiple","Capital in, value out","Total venture raised vs. exit value for the two fiber-adjacent exits.", legend([("#EBDDF8","Raised",0),("#EF5B2B","Exit value",0)])) +
                   figure("chCategory","Disclosed capital by category","Sum of disclosed funding in the company database, $M. Excludes WHOOP's $575M round."),
        extra_charts=[{"type":"pairbars","id":"chMultiple","unit":"$M","max":2000,"labelW":80,"colors":["#EBDDF8","#EF5B2B"],"rows":[["Poppi",40,1950,"Raised ","Exit "],["Grüns",55,1200,"Raised ","Exit "]]},
                      {"type":"category","id":"chCategory","thesis":"fiber","exclude":["WHOOP"]}])
    land, lch = landscape_section("Fiber", [
      ["Floura",3.2,8.9,"r",3,"w"],["38TERA",1.9,8.1,"r",0,"w"],["Myota",2.7,7.4,"l",4.5,"w"],["Bellway",3.9,6.9,"r",8.2,"w"],["Supergut",5.7,8.0,"r",0,"w"],
      ["BelliWelli",5.8,6.7,"r",26.4,"w"],["One Bio",4.5,6.0,"l",44,"w"],["COMET",3.6,5.5,"l",22,"w"],["Hero Bread",7.1,5.4,"r",47.5,"w"],["Tiny Health",6.6,6.1,"r",46,"e"],
      ["Epetōme",2.4,6.2,"l",0,"e"],["CarobWay",1.6,3.8,"r",0,"e"],["That's it.",6.9,3.6,"r",0,"e"],["Magic Spoon",7.4,2.7,"r",85,"i"],["Olipop",8.7,3.7,"l",89.7,"i"],
      ["Grüns",9.2,1.6,"l",55,"a"],["Poppi",9.7,0.9,"l",40,"a"],["Metamucil (P&G)",9.8,0.4,"l",0,"i"],["Benefiber (Haleon)",8.4,0.9,"l",0,"i"]])
    dots = '<script>(function(){var g=document.getElementById("grid");if(!g)return;for(var i=0;i<100;i++){var d=document.createElement("span");d.className="dot"+(i<5?" hit":(i<10?" maybe":""));d.style.setProperty("--i",i);g.appendChild(d);}})();</script>'
    F = [["Fiber gummies",1.86,.1144,'#1C1B1F'],["Fiber and prebiotic ingredients",8.9,.082,'#5B3E86'],["Fiber supplements",4.76,.068,'#C9B1E8'],["U.S. supplements (total)",77.5,.0597,'#BDB6AE'],["Psyllium",1.47,.0391,'#F2A07B']]
    charts = dch + [lch,
      {"type":"lines","id":"chIndex","start":2026,"end":2031,"legend":"lgIndex","series":[[f[0],f[2],f[3]] for f in F]},
      {"type":"pairbars","id":"chSize","unit":"$B","max":14,"labelW":190,"rows":[[f[0],f[1],round(f[1]*(1+f[2])**5,1)] for f in F if 'U.S.' not in f[0]]},
      {"type":"quadrant","id":"chOpp","H":360,"xa":2,"xb":10,"ya":1,"yb":10,"quads":[[5,10,5,10,'Most attractive','#EBDDF8']],"xl":"Growth momentum →","xs":"Momentum →","yl":"Open space (fewer scaled players) →","ys":"Open space →",
       "points":[["GLP-1 companion",8.8,7.3,"l"],["Fiber tracking in apps",6.4,8.9,"r"],["Ingredient IP",7.6,6.2,"r"],["Kids' fiber",5,8.1,"r"],["Clinical and IBS formats",5.6,5.5,"r"],["Gummies and new formats",9.2,4.4,"l"],["Fortified snacks",6.4,3.3,"r"],["Prebiotic soda",6,2.2,"r"],["Psyllium powders",3,1.6,"r"]]}]
    body = h + sec["summary"] + sec["science"] + dots + sec["types"] + sec["rules"] + sec["market"] + sec["outlook"] + deals + land + sec["funds"] + sec["strategics"] + sec["voices"] + sec["thesis"] + sec["risks"] + sec["sources"] + pagenext(None, THESES[1])
    return body, charts

# ======================= HOME =======================
CARDS = [
 ("fiber","Fiber is the next protein","Most Americans miss their fiber target. GLP-1 use and tracking make the gap visible, and strategics are paying up for gut health.",[("$3.15B+","fiber-adjacent exits since 2025"),("5–10%","of adults hit the fiber target"),("+11.4%","fiber gummies CAGR")],"Floura, Supergut, Myota"),
 ("nonalc","Moderation is the market","Drinking hit a 90-year low. Big alcohol is buying what replaces the drink, led by functional social tonics like Hiyo.",[("54%","of U.S. adults drink, a record low"),("$20.8M","Hiyo Series B, Oct 2026"),("+18%/yr","U.S. NA beer volume forecast")],"Hiyo, TRIP, Ghia"),
 ("meat","Real meat is back","New guidelines nearly doubled the protein target. Meat sticks took over meat snacks while plant-based meat shrank.",[("$5.5B","U.S. meat snacks, 2025"),("54.4%","meat sticks' share of category"),("-26%","plant-based meat sales over two years")],"Singing Pastures, New Primal, Primal Queen"),
 ("wear","Health tech you wear like jewelry","Women are the core smart ring customer. Earrings, ring jewelry, and women's health software are the next layer.",[("72%","of Oura members are women"),("~$11B","Oura private valuation"),("$1.55B","record women's health equity, 2025")],"Lumia, Incora Health, Mira"),
]
PICKS = [("Floura","fiber","Untapped","National Starbucks launch on a few million raised."),("Supergut","fiber","Breakout","Clinical study plus a GLP-1 booster."),
         ("Hiyo","nonalc","Breakout","Constellation led its $20.8M Series B."),("TRIP","nonalc","Breakout","$40M raise; targeting $200M revenue in 2026."),
         ("Singing Pastures","meat","Untapped","Female-founded meat sticks; backed by Bullish."),("New Primal","meat","Breakout","Roadmap to $100M+ retail sales in 2026."),
         ("Lumia","wear","Untapped","Smart earrings for blood flow, sleep, and cycle."),("Incora Health","wear","Untapped","Fertility earring with a clinical trial at seed.")]

def home():
    tn = {k: (n, p, c) for k, n, p, c in THESES}
    ops = ''.join(f'<li><a class="opp" href="companies.html#co-{slug(n)}"><span class="rk">{i+1}</span><span class="ob"><strong>{E(n)}</strong><span class="tag">{E(tn[t][0])}</span><em>{E(w)}</em></span></a></li>' for i, (n, t, tag, w) in enumerate(PICKS))
    hero_html = f'''<div class="wrap">
<header class="hero">
  <div>
    <span class="eyebrow"><i></i>Consumer venture research</span>
    <h1>Sarina's <em>Venture</em> Thesis</h1>
    <p class="sub">Four consumer theses from an operator turned investor: fiber as the next protein, the moderation economy, the return of real meat, and discreet wearables for women's health. Each one comes with the data, deals, investors, and companies behind it.</p>
    <p class="meta"><span>By Sarina Sherman, Columbia Business School</span><span class="sep"></span><span>Updated {UPDATED}</span><span class="sep"></span><span>{len(COMPANIES)} companies tracked</span></p>
    <div class="ctas"><a class="p" href="#theses">Explore the theses</a><a class="s" href="companies.html">Open the company database</a></div>
  </div>
  <aside class="topops" aria-labelledby="topopsT">
    <div class="topops-head"><h2 id="topopsT">Top VC opportunities</h2><a href="companies.html#watch" class="seeall">Full watch list</a></div>
    <ol>{ops}</ol>
    <p class="topops-note">Author's picks, two per thesis. Select a company to open its profile.</p>
  </aside>
</header>
<div class="typeband" aria-hidden="true"><div><span>Fiber</span><em>Non-alc</em><span>Meat</span><em>Wearables</em><span>Fiber</span><em>Non-alc</em></div></div>
<div class="facts"><div><b>5–10%</b><span>of U.S. adults hit their daily fiber target</span></div><div><b>54%</b><span>of U.S. adults say they drink, a 90-year Gallup low</span></div><div><b>54.4%</b><span>of meat snack dollars now go to meat sticks</span></div><div><b>72%</b><span>of Oura's members are women</span></div></div>
</div>
'''
    cards_html = ''
    for k, h3, p, stats, picks in CARDS:
        n, pg, c = tn[k]
        st = ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in stats)
        cards_html += f'<a class="thcard" href="{pg}" style="--ac:{c};text-decoration:none;color:inherit"><span class="eyebrow"><i style="background:{c}"></i>{n}</span><h3>{h3}</h3><p>{p}</p><div class="thstats">{st}</div><p class="thpicks"><strong>Watching:</strong> {picks}</p><span class="go" style="color:var(--taupe-deep)">Read the {n.lower()} thesis</span></a>'
    theses = section("theses","Four theses", "Each thesis page has the same structure: why now, the category map, regulation, market and outlook, deal flow, a company landscape, investors, strategics, voices, the thesis itself, and risks.", f'<div class="thgrid">{cards_html}</div>')
    allds = []
    for k, ds in DEALS.items():
        for d in ds: allds.append((d[0], k, d))
    allds.sort(key=lambda x: x[0], reverse=True)
    rows, tags = [], []
    for key, k, d in allds[:14]:
        n, pg, c = tn[k]
        rows.append([d[1], f'<strong>{E(d[2])}</strong><span class="sub">{E(d[3])}</span>', f'<a class="thchip" href="{pg}#deals"><i style="background:{c}"></i>{n}</a>', E(d[4]), E(d[5])])
        tags.append(k)
    ctl = '<div class="controls" role="group" aria-label="Filter deals by thesis"><button class="flt" data-g="hd" data-f="all" aria-pressed="true">All</button>' + ''.join(f'<button class="flt" data-g="hd" data-f="{k}" aria-pressed="false"><i class="dot" style="background:{c}"></i>{n}</button>' for k, n, p, c in THESES) + '</div>'
    deals = section("deals","Latest deals across theses","The most recent raises, exits, and strategic moves, newest first.", ctl + table(["When","Company","Thesis","Deal","Backers or buyer"], rows, 820, fg="hd", tags=tags))
    lens = section("lens","How I evaluate a consumer company","The same four questions run through every thesis, shaped by running Amazon and Walmart PPC and building a food brand from a cold pitch.",
        '<div class="lens"><div><b>Habit</b><p>Does the product earn a daily or weekly spot? I look at 90-day repeat and subscription retention before topline growth.</p></div><div><b>Distribution edge</b><p>Is there a channel the brand owns, from venues and GLP-1 prescribers to Amazon rank and retail velocity per store?</p></div><div><b>Proof</b><p>Clinical data, regulatory standing, or validated accuracy that a fast follower cannot copy.</p></div><div><b>Exit path</b><p>Which strategic needs this brand, and are they already investing in the category?</p></div></div>')
    about = '''<section id="about">
<div class="wrap about">
  <div>
    <h2>About the author</h2>
    <p class="lede">I'm Sarina Sherman, a first-year MBA at Columbia Business School pursuing venture capital in female-focused wellness and consumer brands.</p>
    <p>I read consumer companies the way an operator does. Running Amazon and Walmart PPC showed me how brands win or lose on SKU-level unit economics. Building Prepped n' Plated's brand from a cold pitch taught me that community-rooted distribution is what earns trust for a habit-forming health product. If you're building or investing in any of these categories, I'd love to compare notes.</p>
    <div class="contact-row">
      <a class="cta" href="mailto:ssherman28@gsb.columbia.edu">Email me</a>
      <a class="cta ghost" href="https://www.linkedin.com/in/sarina-sherman/" target="_blank" rel="noopener">Connect on LinkedIn</a>
    </div>
    <ul class="contact">
      <li><span>Email</span><a href="mailto:ssherman28@gsb.columbia.edu">ssherman28@gsb.columbia.edu</a></li>
      <li><span>Phone</span><a href="tel:+13129659951">(312) 965-9951</a></li>
      <li><span>LinkedIn</span><a href="https://www.linkedin.com/in/sarina-sherman/" target="_blank" rel="noopener">linkedin.com/in/sarina-sherman</a></li>
      <li><span>Portfolio</span><a href="https://sarina-sherman-6.github.io/CBS-MBA-AI-Portfolio/" target="_blank" rel="noopener">sarina-sherman-6.github.io/CBS-MBA-AI-Portfolio</a></li>
      <li><span>Substack</span><a href="https://substack.com/@sarinasherman" target="_blank" rel="noopener">substack.com/@sarinasherman</a></li>
    </ul>
  </div>
  <ul class="flist">
    <li><span>Now</span>Columbia Business School, MBA Class of 2028; Consortium and Forté Fellow</li>
    <li><span>Brand and Sales Director</span>Prepped n' Plated, women-owned Chicago meal prep and catering</li>
    <li><span>E-Commerce Brand Manager</span>Marshall Associates, Amazon and Walmart PPC</li>
    <li><span>Also</span>Wayfair alum; ACE-certified group fitness instructor</li>
  </ul>
</div>
</section>
'''
    nfund = len([c for c in COMPANIES if c.get("raisedM")])
    nwatch = len([c for c in COMPANIES if c.get("watch")])
    band = f'''<section class="dbsec" style="border-top:none"><div class="wrap"><div class="dbband">
  <div><span class="eyebrow" style="border-color:#fff;color:#fff"><i style="background:#F9D8C6"></i>The company database</span>
  <h2 style="margin-top:14px">Every company, <em>one table</em></h2>
  <p>{len(COMPANIES)} companies across fiber, non-alc, meat protein, and wearables. Filter by thesis, category, status, and capital raised, sort by latest news, and export to CSV for your own pipeline.</p>
  <div class="ctas"><a class="p" href="companies.html">Open the database</a><a class="s" href="companies.html#watch">See the watch list</a></div></div>
  <div class="stats"><div><b>{len(COMPANIES)}</b><span>companies tracked</span></div><div><b>{nwatch}</b><span>on the watch list</span></div><div><b>{nfund}</b><span>with disclosed funding</span></div><div><b>CSV</b><span>export any filtered view</span></div></div>
</div></div></section>
'''
    return hero_html + band + theses + deals + lens + about, []

# ======================= COMPANIES =======================
def companies():
    btns = '<button class="flt" data-g="th" data-f="all" aria-pressed="true">All theses</button>' + ''.join(f'<button class="flt" data-g="th" data-f="{k}" aria-pressed="false"><i class="dot" style="background:{c}"></i>{n}</button>' for k, n, p, c in THESES) + '<button class="flt" data-g="th" data-f="watch" aria-pressed="false">Watch list</button>'
    counts = ' &middot; '.join(f'{sum(1 for x in COMPANIES if x["thesis"]==k)} {n.lower()}' for k, n, p, c in THESES)
    body = f'''<div class="wrap">
<header class="hero dbhero" style="grid-template-columns:1fr">
  <div>
    <span class="eyebrow"><i></i>Across all four theses</span>
    <h1>Company <em>database</em></h1>
    <p class="sub">Brands, ingredient makers, platforms, and strategics across fiber, non-alc, meat protein, and wearables. Companies tagged Watch are ones I think are worth tracking for a near-term raise or exit.</p>
    <p class="meta"><span>{len(COMPANIES)} companies: {counts}</span><span class="sep"></span><span>Updated {UPDATED}</span></p>
  </div>
</header>
</div>
<section id="database" style="padding-top:8px;border-top:none">
<div class="wrap">
  <div class="controls" role="group" aria-label="Filter by thesis">{btns}</div>
  <div class="controls">
    <label for="q" class="sr">Search companies</label>
    <input id="q" type="search" placeholder="Search by company, investor, or keyword">
    <label class="sel" for="cat"><span>Category</span><select id="cat"><option value="all">Any category</option></select></label>
    <label class="sel" for="sort"><span>Sort by</span><select id="sort"><option value="latest:desc">Most recent news</option><option value="raisedM:desc">Most capital raised</option><option value="name:asc">Company, A to Z</option><option value="category:asc">Category</option><option value="status:asc">Status</option></select></label>
    <label class="sel" for="status"><span>Status</span><select id="status"><option value="all">Any status</option><option value="Private">Private</option><option value="Acquired">Acquired or being acquired</option><option value="Public">Public</option><option value="Corporate">Corporate division</option><option value="Declining">Declining</option></select></label>
    <label class="sel" for="cap"><span>Capital raised</span><select id="cap"><option value="all">Any amount</option><option value="u10">Under $10M</option><option value="10-50">$10M to $50M</option><option value="o50">Over $50M</option><option value="none">Not disclosed</option></select></label>
    <button class="reset" id="reset">Clear filters</button>
    <span class="count" id="count" aria-live="polite"></span>
  </div>
  <div class="exportbar" role="group" aria-label="Export the database">
    <strong>Export</strong>
    <button class="xbtn" id="xView" type="button">Download current view (CSV)</button>
    <button class="xbtn alt" id="xAll" type="button">Download all {len(COMPANIES)} (CSV)</button>
    <button class="xbtn alt" id="xCopy" type="button">Copy for Sheets or Excel</button>
    <span class="xmsg" id="xmsg" aria-live="polite">Exports respect your filters, search, and sort.</span>
  </div>
  <div class="tbl">
    <table id="dbTbl" style="min-width:1040px">
      <thead><tr><th><button class="sorth" data-k="name">Company</button></th><th><button class="sorth" data-k="category">Thesis and category</button></th><th>What they do</th><th><button class="sorth" data-k="raisedM">Raised</button></th><th>Key investors</th><th><button class="sorth" data-k="latest">Latest news</button></th><th>Why it matters</th></tr></thead>
      <tbody></tbody>
    </table>
  </div>
  <p class="note mt">Funding data compiled from press releases, filings, CB Insights, PitchBook, and trade press. "Raised" is total disclosed funding; a plus sign means only some rounds are public. A dash means not disclosed. Each thesis page lists its sources.</p>
</div>
</section>
'''
    return body, []

PAGES = [
 ("index.html","Sarina's Venture Thesis","Four consumer venture theses by Sarina Sherman: fiber, non-alc, meat protein, and discreet wearables for women's health.","home",home,False),
 ("fiber.html","Fiber Thesis | Sarina's Venture Thesis","Why fiber is the next protein: science, regulation, market, deals, investors, and companies.","fiber",fiber,True),
 ("non-alc.html","Non-Alc Thesis | Sarina's Venture Thesis","The moderation economy: non-alcoholic beer, spirits, functional tonics, deals, and companies.","nonalc",pages_new.nonalc,False),
 ("meat-protein.html","Meat Protein Thesis | Sarina's Venture Thesis","The return of real meat: meat sticks, organ meat, and the decline of plant-based meat.","meat",pages_new.meat,False),
 ("wearables.html","Wearables Thesis | Sarina's Venture Thesis","Discreet wearables and women's health: smart rings, smart earrings, ring jewelry, and care platforms.","wear",pages_new.wear,False),
 ("companies.html","Company Database | Sarina's Venture Thesis","Searchable database of companies across four consumer venture theses.","db",companies,True),
]

def build(out, artifact):
    os.makedirs(out + '/assets', exist_ok=True)
    for fn, title, desc, cur, fnc, needs_co in PAGES:
        body, charts = fnc()
        html_ = page(title, desc, cur, body, charts, companies=needs_co, artifact=artifact, main=(fn == 'index.html'))
        open(f'{out}/{fn}', 'w').write(html_)
    shutil.copy(os.path.join(ROOT, 'assets', 'site.css'), out + '/assets/site.css')
    shutil.copy(os.path.join(ROOT, 'assets', 'site.js'), out + '/assets/site.js')
    open(out + '/assets/companies.js', 'w').write('window.COMPANIES=' + json.dumps(COMPANIES, ensure_ascii=False) + ';\n')

build(os.path.join(ROOT, 'docs'), False)
if os.environ.get('ART_OUT'):
    build(os.environ['ART_OUT'], True)
print('ok', len(COMPANIES))
