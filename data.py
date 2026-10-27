import os
import json, re, unicodedata

def slug(n):
    n = unicodedata.normalize('NFKD', n).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', n).strip('-')

K = ["name","category","what","investors","why","watch","status","raisedM","raisedPlus","latest","latestNote"]
def rows(thesis, lst):
    out = []
    for r in lst:
        d = dict(zip(K, r)); d["thesis"] = thesis; d["watch"] = bool(d["watch"]); d["raisedPlus"] = bool(d["raisedPlus"])
        d = {k: v for k, v in d.items() if v is not None and v != ""}
        d["slug"] = slug(d["name"]); out.append(d)
    return out

FIBER = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fiber_rows.json')))
for d in FIBER:
    d["thesis"] = "fiber"; d["slug"] = slug(d["name"])

NONALC = rows("nonalc", [
 ["Hiyo","Functional tonics","Organic social tonic with adaptogens and nootropics, 30 calories a can","Constellation Brands (lead), Live Nation, SG Credit Partners (debt)","On track for 1M+ cases this year; pushing toward 10,000+ doors including Costco, Target, Kroger",1,"Private",39.8,1,"2026-10","$20.8M Series B led by Constellation"],
 ["TRIP","Functional tonics","Adaptogen sparkling drinks built for unwinding","Coefficient Capital plus celebrity investors","Said it was on track for $100M revenue in 2025 and $200M in 2026",1,"Private",40,1,"2025-11","$40M raise"],
 ["Recess","Functional tonics","Calming sparkling water and mood drinks","Not shown","Raised a new round and added leadership; early leader in the mood-drink category",1,"Private",None,0,"2025","New funding round"],
 ["Neutonic","Functional tonics","Functional energy and focus drinks","Not shown","Named among social and functional brands recently raising",0,"Private",None,0,None,""],
 ["The Calmer Co","Functional tonics","Kava-based relaxation products from Pacific Island supply chain","Novus Capital (lead manager)","Raising to expand U.S. wholesale and Amazon; kava as an alcohol alternative",0,"Public",1.6,1,"2026-02","$1.6M placement for U.S. expansion"],
 ["Athletic Brewing","NA beer","Largest dedicated non-alcoholic brewery in the U.S.","General Atlantic, Keurig Dr Pepper","Around $800M valuation; held 19%+ of NA beer and drove about a third of its growth (NIQ, 2024)",0,"Private",251,1,"2024-07","$50M led by General Atlantic"],
 ["Collider Brew Co","NA beer","Adaptogen and functional-mushroom NA beer (UK)","DMG Ventures, SyndicateRoom","NA beer plus function; pre-seed beat its target",1,"Private",0.9,0,"2024-11","£720K pre-seed"],
 ["HOPWTR","Hop water","Calorie-free sparkling hop water with adaptogens and nootropics","Constellation Ventures (2021), then acquired","Constellation bought the remaining stake after a venture investment, the playbook in action",0,"Acquired",None,0,"2026-03","Constellation agrees to buy remaining stake"],
 ["Ghia","NA spirits","Non-alcoholic aperitif and spritz, founded by Mélanie Masarin","Not shown","Category-defining NA aperitif with strong brand and on-premise presence",1,"Private",None,0,None,""],
 ["Three Spirit","NA spirits","Functional plant-based elixirs (Livener, Social, Nightcap)","CircleUp","First functional NA spirit in UK grocery (Waitrose, 2026)",0,"Private",3.7,1,"2026-06","Waitrose launch"],
 ["Cann","Hemp THC drinks","Microdosed THC social tonic","Not shown","Federal hemp THC limit hits in November 2026; CEO calls it a one-year shot clock for real rules",0,"Private",None,0,"2025-11","Federal hemp THC limit passed"],
 ["Cycling Frog","Hemp THC drinks","THC seltzers","Not shown","Founding member of a Colorado coalition pushing for THC beverage rules",0,"Private",None,0,"2026-04","Colorado THC Beverage Coalition"],
 ["Constellation Brands NA portfolio","Strategics","Corona Non-Alcoholic, Kim Crawford Illuminate, Modelo Chelada NA, HOPWTR","Constellation Brands","The most active strategic: venture stakes that convert to acquisitions",0,"Public",None,0,"2026-03","HOPWTR acquisition"],
 ["Live Nation New Ventures","Strategics","Equity stakes plus pouring rights at venues and festivals","Live Nation","Backs Hiyo, Liquid Death, Owen's; Athletic is its NA beer partner at 100+ venues",0,"Public",None,0,"2025-12","Hiyo equity and venue partnership"],
 ["Heineken 0.0","Strategics","Global NA lager","Heineken","Incumbent benchmark for NA beer at scale",0,"Public",None,0,None,""],
])

MEAT = rows("meat", [
 ["Chomps","Meat sticks","Clean-label grass-fed beef and turkey sticks","Co-investments with Western Smokehouse Partners and Landmark Snacks","161% sales growth vs. 16.1% for the category; reported to be filling only 85% of orders",0,"Private",None,0,"2025-10","Nebraska plant announced"],
 ["Archer","Meat sticks","Grass-fed beef, turkey, and now chicken sticks","Not shown","Sales up 57% in 2025; set a $300M sales goal for 2025",0,"Private",None,0,"2026-04","Star Wars collab and chicken launch"],
 ["New Primal","Meat sticks","Clean-label sticks, including kids' minis at Aldi","Not shown","Roadmap to $100M+ retail sales in 2026 across about 15,000 doors; tripled capacity",1,"Private",21.2,1,"2026-06","Named Processor of the Year"],
 ["Singing Pastures","Meat sticks","Female-founded meat sticks built for women on the go","Bullish","Targets women, one of the fastest-growing on-the-go protein segments",1,"Private",None,0,"2026-04","Bullish investment"],
 ["Righteous Felon","Meat sticks","Craft jerky and meat sticks","GroundForce Capital","Backed by the fund behind Liquid Death and OWYN",1,"Private",None,0,"2026","GroundForce investment"],
 ["Mighty Spark","Meat sticks","Specialty meat snacks and sausages","Swander Pace Capital, Branch Brook Holdings","PE roll-up comp for the category",0,"Acquired",None,0,"2021-05","Acquired by Swander Pace"],
 ["4505 Meats","Meat sticks","Pork rinds and meat snacks","Benestar Brands (acquirer)","Sold to a holding company planning to expand beyond meat snacks",0,"Acquired",None,0,None,""],
 ["Jack Link's","Strategics","Category's legacy leader in jerky and sticks","Family-owned","Lost 573 basis points of share in 2025 as better-for-you brands grew",0,"Private",None,0,None,""],
 ["Good Warrior (PepsiCo)","Strategics","PepsiCo's first standalone beef stick brand","PepsiCo","A top strategic entered the category in March 2026, a signal of future M&A",0,"Public",None,0,"2026-03","Brand launch"],
 ["Kroger Simple Truth sticks","Strategics","Private-label clean-label beef sticks","Kroger","Retailer private label arriving is a sign of category maturity",0,"Public",None,0,"2026-01","24 Simple Truth Protein launches"],
 ["Ancestral Supplements","Organ meat","Freeze-dried grass-fed beef organ capsules","Not shown","Long-standing category leader on Amazon",0,"Private",None,0,None,""],
 ["Heart & Soil","Organ meat","Organ supplements from regenerative cattle","Founded by Dr. Paul Saladino","Influencer-led brand with heavy search interest",0,"Private",None,0,None,""],
 ["Primal Queen","Organ meat","Beef organ supplement formulated for women","Not shown","Led Amazon beef-organ sales in July 2026 by monthly volume",1,"Private",None,0,"2026-07","Top Amazon seller in category"],
 ["Force of Nature Meats","Organ meat","Regenerative ground beef blended with liver and heart","Not shown","Organ meat in a format people already cook with",0,"Private",None,0,None,""],
 ["Beyond","Plant-based","Plant-based meat, now rebranded as a plant protein company","Public","Q4 2025 revenue fell about 20%; gross margin dropped to 2.8% in 2025",0,"Declining",None,0,"2026-03","Rebrand to Beyond, The Plant Protein Co."],
 ["Impossible Foods","Plant-based","Plant-based burgers, sausage, and chicken","Not shown","CEO stepped down; company floated a hybrid half-beef burger",0,"Declining",None,0,"2026","CEO transition"],
])

WEAR = rows("wear", [
 ["Oura","Smart rings","Smart ring plus membership; sleep, cycle, pregnancy, and metabolic insights","Fidelity (lead, 2025), Dexcom, Forerunner Ventures","About 72% of members are women; 5.7M paid members; postponed a $2.2B IPO on Sep 29, 2026",0,"Private",1500,1,"2026-09","IPO postponed"],
 ["Ultrahuman","Smart rings","Titanium ring with no subscription; Ring Pro shipping in the U.S.","Not shown","About $140M annualized revenue (Sacra); demand ran far ahead of U.S. supply",1,"Private",70,1,"2026-09","$70M round"],
 ["Circular","Smart rings","Smart ring; Ring 3 Pro and Slim due in early 2027","Not shown","Positioning around an FDA-cleared ECG feature",0,"Private",None,0,None,""],
 ["Movano Evie","Smart rings","Women-first smart ring, $269, no subscription","Public (Nasdaq: MOVE)","Early women-specific ring; a useful lesson in how hard hardware distribution is",0,"Public",None,0,None,""],
 ["Samsung Galaxy Ring","Strategics","Ring bundled into the Galaxy ecosystem","Samsung","Ring 2 likely pushed to 2027 amid patent fights",0,"Public",None,0,None,""],
 ["Lumia","Smart earrings","Smart earrings tracking blood flow, sleep, temperature, and cycle","Not shown","Team from Bose, Peloton, WHOOP and Philips; Lumia 2 launched with new funding",1,"Private",7,1,"2025-11","$7M raise and Lumia 2 launch"],
 ["Incora Health","Smart earrings","Fertility-focused earring tracking basal temperature, HRV, and sleep","Medical school partnership; seed investors","Completed a clinical trial before launch, rare at seed stage",1,"Private",0.5,1,None,""],
 ["Zura Health","Smart earrings","AI coach for active women paired with a smart earring (Munich)","EXIST program","Founded 2026; aims at fertility, perimenopause, and prevention",0,"Private",None,0,"2026-08","Profiled by Munich Startup"],
 ["LIL Milan","Ring accessories","Handmade fine-jewelry Cover Ring for Oura Ring 4","Founder-owned","A fine jeweler entering the smart-ring layer",0,"Private",None,0,"2025-11","Cover Ring launch"],
 ["Steff Eleoff","Ring accessories","Handcrafted sterling and gold vermeil Oura ring covers","Founder-owned","Independent designer building a jewelry layer on Oura's installed base",1,"Private",None,0,"2026-04","Featured in Grazia"],
 ["OSleeve","Ring accessories","Protective sleeves for Oura and Ultrahuman rings","Not shown","Utility accessory for active wear",0,"Private",None,0,None,""],
 ["Mira","Women's health platforms","At-home hormone testing","Not shown","Lab-grade hormone data integrated into Oura (Feb 2026)",1,"Private",None,0,"2026-02","Oura partnership"],
 ["Midi Health","Women's health platforms","Virtual menopause and midlife care","Not shown","Oura care partner; insurance-covered midlife care at scale",0,"Private",50,1,"2025-10","$50M Series C"],
 ["NABTA Health","Women's health platforms","Dubai-based at-home diagnostics, virtual visits, and AI care for fertility, pregnancy, and menopause","Phoenix Venture Partners","Moving from direct-to-consumer into employer and insurer partnerships",0,"Private",None,0,"2026-10","Second close of $3M pre-Series A"],
 ["Unravel Health","Women's health platforms","Micro Lab at-home saliva test measuring multiple hormones in minutes (UK)","Conduit EIS Impact Fund and Wrightwood (leads), Leo Capital, Embryo Ventures, Hermesa, Zinc","University of Glasgow spinout; funds go to new markers and the FDA process",0,"Private",3.3,1,"2026-10","£2.5M raise"],
 ["Maven Clinic","Women's health platforms","Virtual women's and family health clinic","Not shown","Oura partner; reported to be eyeing an IPO window",0,"Private",420,1,None,""],
])

COMPANIES = FIBER + NONALC + MEAT + WEAR

# Deals per thesis: (key YYYY-MM, label, company, sub, deal, backers, readthrough, kind r/e/s, $M or None)
DEALS = {
"fiber": [
 ("2026-09","Sep 2026","Tiny Health","Gut microbiome testing","$33M Series B ($46M total)","B Capital (lead), Spero Ventures","Gut data moving toward standard of care","r",33),
 ("2026-06","Jun 2026","Myota","Clinically validated fiber blends","$4.5M Series A","PeakBridge (lead)","Fiber IP going B2B in the U.S.","r",4.5),
 ("2026-06","Jun 2026","Grüns","Gummies with 6 g prebiotic fiber","Unilever buys 80% for €767M; ~$1.2B implied","Unilever","Roughly 4x trailing revenue, under three years from launch","e",1200),
 ("2026-05","2026","Tate & Lyle","Soluble fiber leader","Ingredion agrees to acquire at 595p/share, ~59% premium","Ingredion","Fiber ingredient capacity is consolidating","e",None),
 ("2026-05","May 2026","Nourish","Dietitian care platform","$100M Series C at $1.75B","Menlo (lead), Thrive, Index, JPMorgan growth equity","GLP-1 nutrition support is unicorn-scale","r",100),
 ("2026-04","2026","Epetōme","UK gut health supplements","Multimillion-pound round","Active Partners, Redrice Ventures","Creator-founded brand funding clinical research","r",None),
 ("2026-03","Mar 2026","WHOOP","Wearables and AI insights","$575M at $10.1B","Growth round","The tracking layer is well funded","r",575),
 ("2025-05","May 2025","Poppi","Prebiotic soda","$1.95B ($1.65B net of tax benefits)","PepsiCo; CAVU backed it from seed","About $40M raised; one of the decade's best exits","e",1950),
 ("2025-05","May 2025","Grüns","Series B","$35M at $500M","Headline (lead), Plus Capital, Sugar Capital","Value more than doubled within a year","r",35),
 ("2025-05","May 2025","David","Protein bars","$75M Series A; acquires Epogee","","Brand buys its ingredient supplier","r",75),
 ("2025-03","2025","Olipop","Fiber-forward soda","$50M Series C at $1.85B","","Profitable; 50,000+ doors","r",50),
 ("2025-02","2025","Supergut","GLP-1 booster","Minority growth investment","Full Frame Growth Partners","Clinical proof plus GLP-1 positioning","r",None),
 ("2024-12","Late 2024","One Bio","Short-chain fibers from ag waste","$27M Series A ($44M total)","","GLP-1-friendly ingredient at scale","r",27),
 ("2024-10","Oct 2024","BelliWelli","Fiber powders and bars","$10M Series B ($26.4M total)","Invus","TikTok-native; 405% revenue growth 2023 to 2024","r",10),
 ("2021-08","2021","COMET","Arabinoxylan fiber","$22M Series C","Open Prairie (lead), Louis Dreyfus, BDC Capital, Sofinnova","Patented upcycled fiber; strategic ag investor","r",22),
],
"nonalc": [
 ("2026-10","Oct 2026","Hiyo","Functional social tonic","$20.8M Series B","Constellation Brands (lead), Live Nation","Strategic re-up a year after its first stake","r",20.8),
 ("2026-03","Mar 2026","HOPWTR","Hop water with adaptogens","Constellation buys remaining interest","Constellation Brands","Venture stake from 2021 converts to full acquisition","e",None),
 ("2026-02","Feb 2026","The Calmer Co","Kava relaxation products","$1.6M placement","Novus Capital (lead manager)","Kava gets capital for U.S. wholesale","r",1.6),
 ("2025-12","Dec 2025","Hiyo","Functional social tonic","Equity stake plus multi-year venue deal","Live Nation","Distribution at concerts and festivals","s",None),
 ("2025-11","Nov 2025","TRIP","Adaptogen sparkling drinks","$40M raise","Coefficient Capital, celebrity investors","Targeting $200M revenue in 2026","r",40),
 ("2025-04","Apr 2025","Hiyo","Functional social tonic","Senior debt facility","SG Credit Partners","Debt funds retail expansion","r",None),
 ("2025-02","Feb 2025","Hiyo","Functional social tonic","Minority stake","Constellation Ventures","Big beer bets on functional NA","s",None),
 ("2025-01","Jan 2025","Hiyo","Functional social tonic","$19M round","Constellation Brands and others","Scaling into grocery","r",19),
 ("2024-11","Nov 2024","Collider Brew Co","Adaptogenic NA beer (UK)","£720K pre-seed","DMG Ventures, SyndicateRoom","NA beer plus function","r",0.9),
 ("2024-07","Jul 2024","Athletic Brewing","NA beer","$50M at ~$800M","General Atlantic (lead)","Valuation roughly doubled in two years","r",50),
],
"meat": [
 ("2026-04","Apr 2026","Singing Pastures","Female-founded meat sticks","Investment","Bullish","Consumer investors back women-focused protein","r",None),
 ("2026-03","Mar 2026","Good Warrior","PepsiCo beef sticks","Brand launch","PepsiCo","A top strategic enters meat sticks","s",None),
 ("2026-03","Mar 2026","Beyond","Plant-based meat","Rebrand to Beyond, The Plant Protein Co.","","Plant-based leader drops 'meat' from its name","s",None),
 ("2026-02","2026","Righteous Felon","Craft jerky and sticks","Investment","GroundForce Capital","Fund behind Liquid Death and OWYN enters meat snacks","r",None),
 ("2026-01","Jan 2026","Kroger","Simple Truth beef sticks","Private-label launch","Kroger","Retailer brands arrive as the category matures","s",None),
 ("2025-10","Oct 2025","Chomps","Clean-label meat sticks","New plant with Landmark Snacks (+15% capacity)","Landmark Snacks, bank financing","Capacity, not demand, is the constraint","s",None),
 ("2025-07","Jul 2025","Chomps","Clean-label meat sticks","300,000 sq ft dedicated plant","Western Smokehouse Partners","Co-investment to double production by 2026","s",None),
 ("2021-05","May 2021","Mighty Spark","Specialty meat snacks","Acquired","Swander Pace Capital, Branch Brook","PE comp for the category","e",None),
],
"wear": [
 ("2026-10","Oct 2026","NABTA Health","AI-assisted fertility and menopause care","Second close of $3M pre-Series A","Phoenix Venture Partners","Women's health care shifts toward employer and insurer channels","r",None),
 ("2026-10","Oct 2026","Unravel Health","At-home saliva hormone test","£2.5M raise","Conduit EIS Impact Fund and Wrightwood (leads), Leo Capital, Embryo Ventures, Zinc","Lab-grade hormone data moves into a home device","r",3.3),
 ("2026-09","Sep 2026","Oura","Smart ring","$2.2B IPO postponed (~$15.6B at midpoint)","Goldman Sachs, Morgan Stanley, J.P. Morgan (underwriters)","Profitable and growing ~90%, but chose to wait on valuation","e",2200),
 ("2026-09","Sep 2026","Ultrahuman","Smart ring","$70M round","Not disclosed","Challenger funding as it returns to the U.S.","r",70),
 ("2025-11","Nov 2025","Lumia","Smart earrings","$7M raise","Not disclosed","Earrings as the next form factor","r",7),
 ("2025-10","Oct 2025","Oura","Smart ring","$900M+ at ~$11B","Fidelity (lead)","Valuation roughly doubled in under a year","r",900),
 ("2025-10","Oct 2025","Midi Health","Menopause care","$50M Series C","Not disclosed","Midlife care scales; Oura partner","r",50),
 ("2026-03","Mar 2026","WHOOP","Wearable","$575M at $10.1B","Growth round","Wrist and ring both attract growth capital","r",575),
 ("2024-12","Dec 2024","Oura","Smart ring","$200M Series D at $5.2B","Fidelity, Dexcom","Strategic glucose partner on the cap table","r",200),
],
}
