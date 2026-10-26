from lib import *

C = dict(ink='#1C1B1F', taupe='#5B3E86', sand='#C9B1E8', clay='#EF5B2B', stone='#EBDDF8', olive='#F2A07B', mute='#BDB6AE')
OPPQ = [[5,10,5,10,'Most attractive','#EBDDF8']]

# ======================= NON-ALC =======================
def nonalc():
    col = '#EF5B2B'
    h = hero("nonalc", "Thesis: non-alc and the moderation economy", "Moderation is the market",
        "Americans are drinking less than at any point in Gallup's 90-year record, and big alcohol is buying its way into what replaces the drink. This is the investor's view of non-alcoholic beer, spirits, functional social tonics, and the hemp THC reset.",
        [("Hiyo","Breakout","$20.8M Series B led by Constellation in October 2026; Live Nation also owns a stake."),
         ("TRIP","Breakout","$40M raise; said it was targeting $200M of revenue in 2026."),
         ("Ghia","Untapped","Category-defining NA aperitif with a strong on-premise brand."),
         ("Collider Brew Co","Untapped","NA beer with adaptogens; pre-seed beat its target."),
         ("Recess","Breakout","New funding and leadership; early leader in mood drinks.")],
        [("54%","of U.S. adults say they drink, the lowest in Gallup's 90-year record"),("$1B+","U.S. off-premise sales of NA beer, wine, and spirits in 2025 (NIQ)"),("+18%","forecast annual U.S. NA beer volume growth through 2029 (IWSR)"),("50%","of adults 18 to 34 say they drink, down from 59% in 2023")], col)
    s = summary([
        ("Demand","Drinking hit a 90-year low","54% of adults drink, and for the first time most say moderate drinking is bad for you.","context","Why now"),
        ("Buyers","Big alcohol is buying, not building","Constellation took a stake in Hiyo, then fully acquired HOPWTR after a 2021 venture bet.","strategics","Strategic activity"),
        ("Capital","Functional tonics are raising real rounds","Hiyo raised $20.8M and TRIP raised $40M in the last year.","deals","Deal flow"),
        ("Growth","NA beer compounds while beer shrinks","IWSR sees +18% a year for U.S. NA beer against -3% for beer overall.","outlook","Market and outlook"),
        ("Thesis","Own a feeling and an occasion","Back brands with a functional effect, on-premise reach, and a strategic on the cap table.","thesis","Investment thesis"),
        ("Risks","The hemp THC reset","A federal limit of 0.4 mg THC per container takes effect in November 2026.","rules","Regulation")])
    ctx = section("context","Why drinking is falling","The decline is broad, generational, and tied to health beliefs, which makes it more durable than a Dry January spike.",
      '<div class="two"><div class="callout"><h3>The numbers</h3><p>Gallup found 54% of U.S. adults drank in 2025, below the prior low of 55% set in 1958 and down from 62% in 2023. Adults 18 to 34 fell to 50%. Women dropped 11 points to 51%, faster than men.</p><p>For the first time, a majority (53%) say even one or two drinks a day hurts your health, and Gallup found no sign that marijuana is replacing alcohol.</p></div>'
      '<div class="callout"><h3>Who actually buys non-alc</h3><p>More than 90% of non-alcoholic buyers also buy alcohol, according to NIQ. The customer is a moderator, not an abstainer, which is why NA sits next to beer, wine, and spirits rather than replacing them.</p><p>Live Nation found 6 in 10 fans switch between alcoholic and non-alcoholic drinks during an event. Occasions, not identity, drive the purchase.</p></div></div>'
      + cards([("Beer is losing occasions","IWSR has U.S. beer volume down 3% a year from 2019 to 2024 and forecasts the same decline through 2029."),("Liquor stores are shrinking","NIQ shows U.S. liquor store sales fell 3.4% in 2025 to $110B, with NA and RTDs the exceptions."),("Functional is mainstream","Functional beverage sales rose 147% over four years to $31.3B (NIQ), so NA drinks now compete on what they do, not just what they lack.")]))
    seg = section("segments","Category map","Non-alc is several different businesses with different economics. Filter by where the growth is coming from.",
      '<div class="controls" role="group" aria-label="Filter segments"><button class="flt" data-g="seg" data-f="all" aria-pressed="true">All</button><button class="flt" data-g="seg" data-f="growth" aria-pressed="false">Fastest growing</button><button class="flt" data-g="seg" data-f="strategic" aria-pressed="false">Strategic interest</button><button class="flt" data-g="seg" data-f="risk" aria-pressed="false">Regulatory risk</button></div>' +
      table(["Segment","What it is","Leaders","Signal","Watch-outs"],[
        ["<strong>NA beer</strong>","Beer styles brewed or dealcoholized to under 0.5% ABV","Athletic Brewing, Heineken 0.0, Corona NA","About 80% of NA sales; +19% in 2025 (NIQ)","Crowded; incumbents own shelf and draft lines"],
        ["<strong>Functional social tonics</strong>","Canned drinks with adaptogens and nootropics for a relaxed lift","Hiyo, TRIP, Recess","Hiyo on track for 1M+ cases; TRIP targeting $200M revenue","Ingredient claims scrutiny; velocity can soften"],
        ["<strong>Hop and botanical waters</strong>","Zero-calorie sparkling drinks that mimic a beer occasion","HOPWTR (Constellation)","Acquired by Constellation in 2026","Small base; needs distribution partner"],
        ["<strong>NA spirits and aperitifs</strong>","Spirit analogs and bitter aperitifs for cocktails","Ghia, Three Spirit, De Soi","Only about 6% of NA sales but growing near 70% (NIQ)","High price per bottle confuses shoppers"],
        ["<strong>NA wine</strong>","Dealcoholized wine","Kim Crawford Illuminate","Dollar sales up 41% in a year (CoBank)","Taste gap remains wide"],
        ["<strong>Kava and botanical relaxers</strong>","Drinks and shots built on kava or similar plants","The Calmer Co, Kavahol","Small rounds funding U.S. expansion","Safety and state-level rules vary"],
        ["<strong>Hemp THC drinks</strong>","Low-dose THC seltzers sold outside dispensaries","Cann, Cycling Frog","Fast growth before the federal limit","0.4 mg per container cap from November 2026"]], 860, fg="seg",
        tags=["growth strategic","growth strategic","strategic","growth","growth","",
              "risk"]))
    rules = section("rules","Regulation","Two rule changes shape the next three years: one shuts a door, the other quietly opens one.",
      '<div class="two"><div><h3>The hemp THC reset</h3><ul class="tl">'
      '<li><b>November 2025</b>The bill ending the federal shutdown redefined hemp, capping hemp-derived products at 0.4 mg of THC per container.</li>'
      '<li><b>2026</b>States and brands form coalitions, such as Colorado\'s THC Beverage Coalition with Cycling Frog, to push for a regulated framework.</li>'
      '<li><b>Mid-November 2026</b>The limit takes effect, making most hemp THC drinks federally unlawful unless Congress acts.</li></ul>'
      '<p class="note">Why it matters: shelf space, distributor attention, and consumer demand built by THC drinks will look for a compliant home. Functional tonics are the obvious one.</p></div>'
      '<div><div class="callout"><h3>Health messaging is moving against alcohol</h3><p>The former U.S. Surgeon General called for cancer warning labels on alcohol, and Gallup shows most Americans now believe moderate drinking is harmful. Notably, the 2025 to 2030 Dietary Guidelines dropped their specific limits on alcohol intake, so the shift is coming from consumers more than from policy.</p></div>'
      '<div class="callout"><h3>Functional claims</h3><p>Adaptogens and nootropics are sold as foods and beverages, so brands describe effects like relaxation without disease claims. Expect more scrutiny of doses and ingredient safety as the category grows.</p></div></div></div>')
    out = section("outlook","Market and outlook","Projections apply each source's published growth rate; they show direction and pace, not precise forecasts.",
      '<div class="chartgrid">' + figure("chNaIdx","Projected volume growth, 2024 = 100","IWSR forecasts compounded to 2029. Dashed line is total U.S. beer.", '<div class="legend" id="lgNa"></div>', wide=True)
      + figure("chNaGallup","Share of U.S. adults who drink","Gallup, 2023 vs. 2025.", legend([("#EBDDF8","2023",0),("#1C1B1F","2025",0)]))
      + figure("chNaGrow","Fastest-growing pockets","Latest reported annual dollar growth by segment (NIQ, CoBank).")
      + figure("chNaOpp","Opportunity map","Author's assessment of momentum against open space. Qualitative.", wide=True) + '</div>'
      + cards([("Fastest growth: RTD and spirits","Non-alcoholic RTDs grew 167% in 2024 and NA spirits near 70%, from small bases."),("Biggest pool: NA beer","About 80% of NA dollars sit in beer, and IWSR expects 18% annual volume growth in the U.S. through 2029."),("Most open: functional and live events","Social tonics with real distribution at venues and festivals have strong pull and few scaled leaders.")]))
    deals, dch = deals_section("nonalc","Raises, acquisitions, and strategic stakes, newest first. Constellation appears again and again.")
    land, lch = landscape_section("Non-alc", [
      ["Hiyo",6.0,7.6,"r",39.8,"w"],["TRIP",7.8,6.6,"l",40,"w"],["Recess",5.6,6.2,"r",0,"w"],["Ghia",3.8,7.8,"r",0,"w"],["Collider Brew Co",1.6,7.0,"r",0.9,"w"],
      ["The Calmer Co",2.2,5.5,"r",1.6,"e"],["Neutonic",3.4,6.4,"r",0,"e"],["Three Spirit",3.4,4.0,"r",3.7,"e"],["Cann",4.4,2.4,"r",0,"d"],["Cycling Frog",2.4,1.6,"r",0,"d"],
      ["Athletic Brewing",8.4,4.0,"l",251,"i"],["HOPWTR",6.8,2.6,"r",0,"a"],["Heineken 0.0",9.6,1.2,"l",0,"i"]])
    funds = section("funds","Who's already writing checks","Strategic venture arms dominate this category, which makes the exit path unusually clear.",
      cards([("Constellation Ventures","Took a minority stake in Hiyo, led its Series B, and converted a 2021 HOPWTR investment into a full acquisition."),
             ("Live Nation New Ventures","Equity plus pouring rights: Hiyo, Liquid Death, Owen's Craft Mixers, with Athletic as NA beer partner at 100+ venues."),
             ("General Atlantic","Led Athletic Brewing's $50M round at roughly $800M, about double its 2022 value."),
             ("Keurig Dr Pepper","Bought a minority stake in Athletic with a $50M investment in 2022."),
             ("Coefficient Capital","Growth-stage consumer fund behind TRIP's $40M raise, alongside celebrity investors."),
             ("CircleUp, DMG Ventures, SG Credit","Early and debt capital: Three Spirit's seed, Collider's pre-seed, Hiyo's debt facility.")]))
    strat = section("strategics","What the big players are doing","Big alcohol needs growth, and non-alc is one of the only parts of the business that has it.",
      cards([("Constellation Brands","Corona Non-Alcoholic, Kim Crawford Illuminate, Modelo Chelada NA, plus Hiyo and HOPWTR. Its beer chief calls NA one of the fastest-growing areas of beverage alcohol."),
             ("Heineken","Heineken 0.0 set the global template for NA beer and remains the incumbent benchmark."),
             ("Live Nation","Turns venues into distribution, investing in the brands it pours."),
             ("Keurig Dr Pepper","Owns part of Athletic, the category's largest independent."),
             ("Retailers","Whole Foods sells more Athletic than any other beer brand, alcoholic or not, per the WSJ."),
             ("Cannabis and beer wholesalers","Hemp THC created odd alliances; the ban will reshuffle what distributors push next.")]))
    vo = section("voices","Who's shaping the conversation", None, voices([
      ("Said the HOPWTR deal fits because NA is one of the fastest-growing areas of total beverage alcohol.","Jim Sabia","President, Beer Division, Constellation Brands",0),
      ("Called the Live Nation partnership a defining moment for the brand.","Evan Quinn","Co-founder and CEO, Hiyo",0),
      ("Notes fans celebrate with alcohol, without it, and often both during the same show.","Tom Allison","SVP, New Ventures, Live Nation",0),
      ("Ties the drop in drinking to a growing belief that moderate alcohol is unhealthy.","Lydia Saad","Director of U.S. Social Research, Gallup",0),
      ("Called the hemp limit “a one-year shot clock” to finally get real rules.","Jake Bullock","Co-founder and CEO, Cann",0),
      ("Expects competition between alcohol, NA drinks, and cannabis beverages to intensify, not settle.","Billy Roberts","Senior Economist, CoBank",1)]))
    th = thesis_section("Moderation is the market. The winners give people a reason to say yes at the moment they would have ordered a drink: a felt effect, a credible social occasion, and distribution wherever alcohol is sold. Strategic alcohol companies are the natural buyers, so the best bets already have one on the cap table.",
      [("Functional beats imitation","Tonics that create a feeling outgrow spirit clones that only remove alcohol and charge spirit prices."),
       ("Venues are the distribution unlock","Live Nation and on-premise deals put brands in the exact moment of choice."),
       ("Strategic venture arms are the exit","Constellation's stake-then-acquire pattern with HOPWTR is the playbook to underwrite."),
       ("The THC reset frees shelf space","Compliant tonics can capture demand built by hemp drinks after November 2026."),
       ("Women are leading the shift","Women's drinking fell faster than men's, making female-founded and female-focused brands a natural fit."),
       ("Cans over bottles","RTD formats grow fastest and fit both grocery and venues.")],
      ["Velocity per store per week","90-day repeat","Share of sales in alcohol channels","On-premise and venue doors","A strategic partner or investor","Transparent functional doses","Gross margin after slotting"],
      ["Brands that depend on hemp THC with no plan for November 2026","Premium NA spirit clones with weak repeat","DTC-only brands without retail or venue distribution"],
      "Functional tonics aimed at women, who are cutting back fastest. Compliant relaxation drinks positioned for the post-ban THC customer. Venue-first brands built with promoters and hospitality groups. Better NA wine, where the taste gap still leaves room for a breakout.")
    risks = risks_section([
      ("The hemp THC ban","A 0.4 mg per container limit takes effect in November 2026.","No dependence on hemp THC, or a dispensary and state-licensed path"),
      ("Ingredient and claims scrutiny","Kava, ashwagandha, and similar botanicals draw safety questions as volumes grow.","Third-party testing, conservative doses, and effect language without disease claims"),
      ("Seasonality","NIQ still sees a January spike in NA sales.","Year-round occasions like concerts, sports, and dinners"),
      ("Incumbent brands","Corona NA, Heineken 0.0, and Kim Crawford Illuminate sit on the same shelves.","A distinct functional effect and community the majors cannot copy quickly"),
      ("Price resistance","Shoppers balk at spirit-level prices for NA bottles.","Cans and lower price points; cocktail use on-premise"),
      ("Velocity softness","BevNET noted Hiyo's sales metrics softened in one quarter even as it raised.","Track per-store velocity and repeat, not door counts")])
    srcs = sources_section([
      src("Gallup via NPR / Michigan Public","2025, August 13","Percentage of Americans who say they drink alcohol hits record low","https://www.michiganpublic.org/2025-08-13/percentage-of-americans-who-say-they-drink-alcohol-hits-record-low-gallup-says"),
      src("Just Drinks","2025, August 14","US adult alcohol consumption rate hits record low","https://www.just-drinks.com/newsletters/us-alcohol-consumption-low"),
      src("PhillyVoice","2025, August 14","Americans are abstaining from alcohol at a record rate","https://www.phillyvoice.com/alcohol-drinking-americans-record-low-gallup/"),
      src("BeverageDaily","2026, April 17","Non-alcohol beer, wine and spirits: US growth potential","https://www.beveragedaily.com/Article/2026/04/17/non-alcohol-beer-wine-and-spirits-us-growth-potential/"),
      src("Yahoo Finance","2026","Declines in alcohol use have hit U.S. liquor sales","https://finance.yahoo.com/news/declines-alcohol-hit-nj-u-081425866.html"),
      src("Drinks Intel / IWSR","2025, July 25","Why alcohol-free has a crucial role to play for beer in the US","https://drinks-intel.com/beer/why-alcohol-free-has-a-crucial-role-to-play-for-beer-in-the-us-consumer-intel/"),
      src("Spherical Insights","2026","Low and no alcohol beverages growth","https://www.sphericalinsights.com/blogs/low-and-no-alcohol-beverages-growth-how-drinking-less-is-reshaping-the-global-beverage-market"),
      src("Vinetur / CoBank","2025","Non-alcoholic beer sales surge 22%","https://www.vinetur.com/en/amp/2025103192853/non-alcoholic-beer-sales-surge-22-as-nearly-half-of-americans-cut-back-on-drinking.html"),
      src("TradedVC","2026, October 5","Hiyo secures $20.8 million in Series B led by Constellation Brands","https://traded.co/vc/deal/hiyo-secures-20-8-million-in-series-b-funding-led-by-constellation-brands/"),
      src("Fitt Insider","2026","Hiyo raises $20.8M to scale social tonics","https://insider.fitt.co/hiyo-raises-20-8m-to-scale-social-tonics/"),
      src("BevNET","2025","Constellation Brands takes minority stake in Hiyo","https://www.bevnet.com/spirits/2025/constellation-brands-takes-minority-stake-in-hiyo-non-alc-functional-rtd-brand"),
      src("BevNET","2025, December","Hiyo lands investment, multi-year partnership with Live Nation","https://www.bevnet.com/news/2025/hiyo-lands-investment-multi-year-partnership-with-live-nation"),
      src("Live Nation","2025","Hiyo brings feel-good social tonics to fans across the U.S.","https://news.livenationentertainment.com/news/hiyo-brings-feel-good-social-tonics-to-fans-across-the-u-s"),
      src("ABF Journal","2025","SG Credit Partners provides debt facility to Hiyo","https://www.abfjournal.com/?p=149223"),
      src("Food Business News","2026, April 1","Constellation Brands to add Hopwtr to non-alcoholic portfolio","https://www.foodbusinessnews.net/articles/30080-constellation-brands-to-add-hopwtr-to-non-alcoholic-portfolio"),
      src("Gama Consumer","2026, April 1","Constellation Brands to fully acquire HOP WTR","https://www.gamaconsumer.com/usa-constellation-brands-fully-acquire-hop-wtr/"),
      src("Athletech News","2025, November 10","Trip raises $40M amid functional drink craze","https://athletechnews.com/calming-beverage-brand-trip-raises-40-million-amid-functional-drink-craze/"),
      src("Food Dive","2024","Athletic Brewing closes $50M round","https://www.fooddive.com/news/nonalocholic-beer-athletic-investors-50-millionnt/720845/"),
      src("Axios San Diego","2024, July 9","Athletic Brewing fuels nonalcoholic beer industry","https://www.axios.com/local/san-diego/2024/07/09/athletic-brewing-fuels-non-alcoholic-beer-industry"),
      src("BevNET","2025, November","Where do hemp THC drinks go from here?","https://www.bevnet.com/news/2025/where-do-hemp-thc-drinks-go-from-here"),
      src("AP via WEAR-TV","2025, November 28","What a federal ban on THC-infused drinks could mean","https://weartv.com/news/nation-world/what-a-federal-ban-on-thc-infused-drinks-and-snacks-could-mean-for-the-hemp-industry-11-28-2025"),
      src("Vicente LLP","2026","Hemp beverages updates","https://vicentellp.com/archive/tags/hemp-beverages"),
      src("Techleap","2026, February","The Calmer Co raises $1.6M","https://finder.techleap.nl/news/feed/the-calmer-co-raises-1-6m-to-accelerate-us-kava-expansion"),
      src("The Drinks Business","2024, November","Collider gets £720k funding boost","https://www.thedrinksbusiness.com/2024/11/non-alcoholic-adaptogenic-beer-collider-gets-720k-funding-boost/"),
      src("VCBacked","2021","Three Spirit funding","https://www.vcbacked.co/company/three-spirit"),
      src("UC Berkeley Public Health","2026","How the nation's new dietary guidelines might backfire","https://publichealth.berkeley.edu/articles/news/commentary/how-new-dietary-guidelines-might-backfire"),
    ])
    charts = dch + [lch,
      {"type":"lines","id":"chNaIdx","start":2024,"end":2029,"legend":"lgNa","series":[["U.S. NA beer volume (IWSR)",0.18,C['ink']],["Global no-alcohol volume (IWSR, 36% over 5 years)",0.0635,C['taupe']],["U.S. total beer volume (IWSR)",-0.03,C['mute'],1]]},
      {"type":"pairbars","id":"chNaGallup","unit":"%","max":70,"labelW":130,"rows":[["All adults",62,54],["Ages 18 to 34",59,50],["Women",62,51],["Men",62,57]]},
      {"type":"hbars","id":"chNaGrow","labelW":120,"rows":[["NA RTDs (2024)",167,"+167%",C['ink']],["NA spirits",70,"~+70%",C['sand']],["NA wine",41,"+41%",C['sand']],["NA beer (2025)",19.2,"+19%",C['sand']]]},
      {"type":"quadrant","id":"chNaOpp","H":360,"xa":2,"xb":10,"ya":1,"yb":10,"quads":OPPQ,"xl":"Growth momentum →","xs":"Momentum →","yl":"Open space (fewer scaled players) →","ys":"Open space →",
       "points":[["Women-led moderation brands",5.4,9.0,"r"],["Live-event and on-premise",6.6,8.0,"r"],["Functional social tonics",8.2,6.8,"l"],["Hop and botanical waters",5.8,5.8,"r"],["NA beer",8.8,4.2,"l"],["NA wine",6.2,3.6,"r"],["Kava and botanical relaxers",3.8,6.6,"r"],["NA spirit clones",3.0,3.0,"r"],["Hemp THC drinks",3.8,1.8,"r"]]}]
    body = h + s + ctx + seg + rules + out + deals + land + funds + strat + vo + th + risks + srcs + pagenext(THESES[0], THESES[2])
    return body, charts

# ======================= MEAT =======================
def meat():
    col = '#7A2E3B'
    h = hero("meat","Thesis: the return of meat protein","Real meat is back",
        "New dietary guidelines nearly doubled the protein target, GLP-1 users are chasing protein per bite, and shoppers want short ingredient lists. Meat sticks are winning, organ meat is the frontier, and plant-based meat is the cautionary tale.",
        [("Singing Pastures","Untapped","Female-founded meat sticks for women; just backed by Bullish."),
         ("New Primal","Breakout","Roadmap to $100M+ retail sales in 2026; kids' sticks at Aldi."),
         ("Primal Queen","Untapped","Female-formulated organ supplement leading Amazon sales."),
         ("Righteous Felon","Untapped","Craft meat snacks backed by the fund behind Liquid Death."),
         ("Heart & Soil","Breakout","Influencer-led organ supplements with heavy search interest.")],
        [("$5.5B","U.S. meat snack sales in 2025, up 6.6% (BofA)"),("54.4%","meat sticks' share of meat snack dollars, up from 37.9% in 2022"),("1.2–1.6 g","protein per kg per day in the new Dietary Guidelines, up from 0.8"),("-20%","Beyond Meat's Q4 2025 revenue decline, year over year")], col)
    s = summary([
        ("Policy","Washington moved protein to the center of the plate","The 2025 to 2030 guidelines call for protein at every meal and include red meat.","rules","Regulation"),
        ("Format","Meat sticks took over meat snacks","Sticks rose from 37.9% to 54.4% of category dollars since 2022 and cost about 30% less per ounce than jerky.","context","Why now"),
        ("Insurgents","Clean-label brands are taking share","Chomps grew 161% while Jack Link's lost 573 basis points of share in 2025.","landscape","Company landscape"),
        ("Contrast","Plant-based meat is shrinking","Refrigerated plant-based sales fell from about $490M in 2021 to $276M in 2025.","outlook","Market and outlook"),
        ("Thesis","Simple protein in snackable formats","Back clean-label brands that own capacity and reach women and kids.","thesis","Investment thesis"),
        ("Risks","Processed-meat health concerns","Critics, including the American Heart Association, push back on red meat.","risks","Key risks")])
    ctx = section("context","Why now","Three forces landed at once: a policy shift, a medication shift, and a label shift.",
      '<div class="two"><div class="callout"><h3>Protein became the organizing principle</h3><p>The 2025 to 2030 Dietary Guidelines raised the protein target to 1.2 to 1.6 grams per kilogram of body weight, about 81 to 109 grams a day for a 150-pound adult, and told Americans to eat protein at every meal from sources that now explicitly include red meat.</p><p>Fortune and Bank of America called meat snacks the clear winner of the GLP-1 shift, growing 6.6% in 2025 while popcorn declined.</p></div>'
      '<div class="callout"><h3>Short labels win</h3><p>Grass-fed meat snack volumes grew 81% in 2025 (Circana). Jack Link\'s now markets three-ingredient sticks, and Archer grew 57% with clean-label, culinary flavors.</p><p>Plant-based meat moved the other way. NIQ\'s Chris Costagli says shoppers read plant-based labels and found unfamiliar ingredients, added sugar, and high sodium.</p></div></div>'
      + cards([("Sticks beat jerky on value","Meat sticks average $1.26 an ounce vs. $1.80 for jerky, about 30% cheaper, and come individually wrapped."),
               ("Demand outruns supply","Chomps said it could fill only about 85% of orders while producing 2 million sticks a day."),
               ("Organ meat goes mainstream","Search interest in beef organ supplements has grown many times over since 2024, led by ancestral-diet influencers.")]))
    seg = section("segments","Category map","Where the money is moving inside animal protein, and where it is leaving.",
      '<div class="controls" role="group" aria-label="Filter segments"><button class="flt" data-g="seg" data-f="all" aria-pressed="true">All</button><button class="flt" data-g="seg" data-f="growth" aria-pressed="false">Growing</button><button class="flt" data-g="seg" data-f="decline" aria-pressed="false">Declining</button></div>' +
      table(["Segment","What it is","Leaders","Signal","Watch-outs"],[
        ["<strong>Meat sticks</strong>","Shelf-stable, individually wrapped beef, turkey, chicken, or pork sticks","Chomps, Archer, New Primal, Jack Link's","54.4% of meat snack dollars; Chomps +161%","Co-manufacturing capacity; beef costs"],
        ["<strong>Jerky</strong>","Dried whole-muscle meat","Jack Link's, Righteous Felon","Slower than sticks; premium craft brands still raising","Higher price per ounce"],
        ["<strong>Organ supplements</strong>","Freeze-dried liver, heart, kidney in capsules, powders, gummies","Ancestral Supplements, Heart & Soil, Primal Queen","Fast search growth; women-focused formulas topping Amazon","Unproven claims; influencer dependence"],
        ["<strong>Organ-blend whole foods</strong>","Ground beef blended with organs","Force of Nature Meats","Organ nutrition in a familiar format","Small, regional supply"],
        ["<strong>Poultry and pork sticks</strong>","Chicken, turkey, and pork alternatives to beef","Archer chicken, New Primal chicken minis","Broadens the category beyond beef","Flavor and texture still catching up"],
        ["<strong>Plant-based meat</strong>","Burgers, sausage, and chicken made from plants","Beyond, Impossible","Retail sales fell 26% over two years (NIQ)","Processing perception; price premium"]], 860, fg="seg",
        tags=["growth","growth","growth","growth","growth","decline"]))
    rules = section("rules","Regulation and policy","Policy turned from a headwind into a tailwind for animal protein in a single release.",
      '<div class="two"><div><h3>2025 to 2030 Dietary Guidelines</h3><ul class="tl">'
      '<li><b>January 7, 2026</b>USDA and HHS released the new guidelines with an inverted pyramid that puts protein, full-fat dairy, and healthy fats first.</li>'
      '<li><b>Protein</b>Target raised from 0.8 to 1.2 to 1.6 g per kg per day, at every meal.</li>'
      '<li><b>Red meat</b>Now named within recommended protein foods.</li>'
      '<li><b>Saturated fat</b>The 10% of calories cap stays, which critics say clashes with the red meat message.</li></ul></div>'
      '<div><div class="callout"><h3>Industry response</h3><p>The Meat Institute and National Cattlemen\'s Beef Association welcomed the guidelines. The American Heart Association urged people to keep prioritizing plant proteins, seafood, and lean meats.</p></div>'
      '<div class="callout"><h3>Supplements and labels</h3><p>Organ supplements are sold as dietary supplements, so they can make structure and function claims but not disease claims. Grass-fed and clean-label claims are where brands compete, and where substantiation matters.</p></div></div></div>')
    out = section("outlook","Market and outlook","Two curves tell the story: animal protein snacks compounding, plant-based meat shrinking.",
      '<div class="chartgrid">' + figure("chMeatIdx","Projected growth, 2026 = 100","Global meat stick and meat snack forecasts (Research and Markets) against plant-based meat's latest annual decline (GFI). Dashed line extends that decline.", '<div class="legend" id="lgMeat"></div>', wide=True)
      + figure("chMeatShare","Meat sticks' share of meat snack dollars","Circana via Snack Food & Wholesale Bakery.")
      + figure("chMeatPB","Refrigerated plant-based meat, U.S. retail","Annual dollar sales, Circana via 210 Analytics.")
      + figure("chMeatOpp","Opportunity map","Author's assessment of momentum against open space. Qualitative.", wide=True) + '</div>'
      + cards([("Fastest growth: sticks","Meat sticks are forecast to grow faster than any other meat snack format, at about 7% a year globally."),("Biggest pool: protein snacking","U.S. meat snacks reached $5.5B, about 7% of a $74.9B savory snack market (BofA)."),("Most open: women, kids, organ meat","Female-focused sticks, lunchbox formats, and organ nutrition in easy forms have few scaled leaders.")]))
    deals, dch = deals_section("meat","Most meat snack capital moves through private equity, strategic launches, and co-manufacturing deals rather than venture rounds, so sizes are rarely disclosed.")
    land, lch = landscape_section("Meat protein", [
      ["Singing Pastures",2.0,8.4,"r",0,"w"],["Primal Queen",3.2,7.6,"r",0,"w"],["Righteous Felon",3.6,6.4,"r",0,"w"],["New Primal",6.0,7.4,"r",21.2,"w"],
      ["Force of Nature Meats",1.6,5.6,"r",0,"e"],["Heart & Soil",5.6,6.0,"r",0,"e"],["Archer",7.2,5.4,"r",0,"i"],["Chomps",8.6,6.4,"l",0,"i"],["Ancestral Supplements",6.6,3.8,"r",0,"i"],
      ["Mighty Spark",5.6,2.8,"r",0,"a"],["4505 Meats",3.8,2.2,"r",0,"a"],["Jack Link's",9.6,1.6,"l",0,"i"],["Good Warrior (PepsiCo)",8.6,3.0,"l",0,"i"],["Beyond",7.6,0.6,"l",0,"d"],["Impossible Foods",5.0,1.2,"l",0,"d"]],
      "Chomps and Archer have not disclosed outside venture rounds; their scale comes from sales and co-manufacturing partnerships.")
    funds = section("funds","Who's already writing checks","Consumer funds and PE are moving in, and co-manufacturers are investing alongside brands.",
      cards([("Bullish","New York consumer investor and marketing firm; invested in female-founded Singing Pastures in April 2026."),
             ("GroundForce Capital","Founder-led fund behind Liquid Death, OWYN, and Vive Organic; backed Righteous Felon."),
             ("Swander Pace Capital","Food-focused PE that acquired Mighty Spark with Branch Brook Holdings and installed a former Jack Link's sales chief as CEO."),
             ("Western Smokehouse Partners","Co-manufacturer that co-invested in a 300,000 sq ft plant dedicated to Chomps."),
             ("Landmark Snacks","Co-manufacturer building Chomps' Nebraska plant, financed with regional banks."),
             ("Benestar Brands","Holding company that bought 4505 Meats to expand beyond meat snacks.")]))
    strat = section("strategics","What the big players are doing","Incumbents are launching their own clean-label sticks, which usually comes before they start buying.",
      cards([("PepsiCo","Launched Good Warrior beef sticks in March 2026, its first standalone meat snack brand."),
             ("Jack Link's","Repositioning around three-ingredient sticks after losing 573 basis points of share in 2025."),
             ("Kroger","Rolled out Simple Truth clean-label beef sticks among 24 new protein products."),
             ("Tyson","Exited plant-based meat entirely, concluding demand did not justify investment."),
             ("Beyond","Dropped 'meat' from its name in March 2026 and moved into protein drinks."),
             ("Impossible Foods","CEO stepped down; the company floated a hybrid burger made half from beef.")]))
    vo = section("voices","Who's shaping the conversation", None, voices([
      ("“It's just not the moment for plant-based meat.”","Ethan Brown","Founder and CEO, Beyond",0),
      ("Said the sector was “mismarketed and mislaunched” as a climate solution.","Peter McGuinness","Former CEO, Impossible Foods",0),
      ("Says shoppers who read plant-based labels found unfamiliar ingredients, sugar, and sodium.","Chris Costagli","Food thought leader, NIQ",0),
      ("Welcomed guidelines telling families to prioritize protein from meat and poultry.","Julie Anna Potts","President and CEO, Meat Institute",0),
      ("Sees meat snack sales accelerating while growth in other food categories tapers.","CoBank","Knowledge Exchange report on meat snacks",0),
      ("Urges people to limit red meat, butter, and tallow and favor plant proteins and seafood.","American Heart Association","Response to the new guidelines",1)]))
    th = thesis_section("Protein is now the organizing principle of the American diet, and shoppers want it from simple, recognizable sources. The winners turn real meat into convenient daily formats, own enough production capacity to meet demand, and reach the women and families driving protein snacking.",
      [("Clean label takes share","Insurgents like Chomps and Archer are taking share from Jack Link's with short ingredient lists."),
       ("Capacity is the moat","When the leader can fill only 85% of orders, owning or locking up co-manufacturing is a real advantage."),
       ("Women and kids are the growth segments","Singing Pastures, New Primal's lunchbox minis, and Primal Queen target buyers legacy brands ignored."),
       ("Organ meat needs better formats","Capsules got it started; gummies, blends, and familiar foods will take it mainstream."),
       ("Beyond beef","Chicken, turkey, and pork sticks widen the category and ease beef cost pressure."),
       ("Strategics will buy","PepsiCo entered by launching; history says the next step is acquiring a proven brand.")],
      ["Velocity vs. category growth","Repeat and subscribe rates","Contracted co-manufacturing capacity","Raw material sourcing and cost","Ingredient count","Share of sales to women and kids","Retail door growth"],
      ["Plant-based meat analogs","Commodity jerky without a brand","Organ supplements making disease claims"],
      "Female-founded and female-focused meat sticks. Organ meat in gummies, blends, and everyday foods. Poultry and pork sticks with real flavor. Protein snacks designed for GLP-1 users who need protein in small portions.")
    risks = risks_section([
      ("Processed meat health concerns","The WHO classifies processed meat as carcinogenic; the AHA pushes back on red meat.","Clean labels, lower sodium, and transparent sourcing"),
      ("Beef supply and price","Chomps reportedly sources most of its beef from Australia, exposing it to trade and cattle-cycle costs.","Diversified sourcing and poultry or pork lines"),
      ("Capacity constraints","Leaders are building plants to keep up with demand.","Locked-in co-manufacturing and staged capacity"),
      ("Private label and incumbents","Kroger, PepsiCo, and Jack Link's are launching clean-label sticks.","Brand, flavor, and community the majors cannot copy quickly"),
      ("Organ supplement claims","Category built on influencer enthusiasm more than clinical data.","Testing, sourcing transparency, and structure and function claims only"),
      ("Policy reversal","The next guidelines could swing back toward plant proteins.","Products that win on taste and convenience, not policy")])
    srcs = sources_section([
      src("Fortune","2026, February 10","Meat snacks have emerged as the clear winner of America's GLP-1 shift","https://fortune.com/2026/02/10/meat-snacks-have-emerged-as-the-clear-winner-of-americas-seismic-glp-1-consumption-shift-while-popcorn-is-down-bad/"),
      src("Snack Food & Wholesale Bakery","2026, July 22","State of the Industry 2026: Meat snacks are beefing up","https://www.snackandbakery.com/articles/116070-state-of-the-industry-2026-meat-snacks-are-beefing-up"),
      src("Feedstuffs / CoBank","2026, June 2","Rising protein demand drives meat snack growth","https://www.feedstuffs.com/agribusiness-news/rising-protein-demand-drives-meat-snack-growth"),
      src("Research and Markets","2026, January","Meat snacks market share analysis 2026 to 2031","https://www.researchandmarkets.com/reports/4602396/meat-snacks-market-share-analysis-industry"),
      src("Meatingplace","2025","Meat snack maker announces new facility plans","https://meatingplace.com/meat-snack-maker-announces-new-facility-plans/"),
      src("Nosh","2025, October 29","Chomps to open dedicated Landmark Snacks facility","https://www.nosh.com/pr/2025/10/29/chomps-to-open-dedicated-landmark-snacks-facility-to-accelerate-exponential-growth"),
      src("The National Provisioner","2025","Chomps celebrates Missouri manufacturing facility opening","https://www.provisioneronline.com/articles/119210-chomps-celebrates-missouri-manufacturing-facility-opening"),
      src("Simplify / Chomps","2026","Chomps company profile","https://simplify.jobs/c/Chomps"),
      src("2PM","2025, October 12","Deep dive: CPG beef vs. DTC beef","https://2pml.com/2025/10/12/uncapped/"),
      src("The National Provisioner","2026","Meat sticks coverage (New Primal, Singing Pastures, Good Warrior, Kroger)","https://www.provisioneronline.com/articles/keyword/7916-meat-sticks"),
      src("Nosh","2026","Meat snacks coverage (Good Warrior, Righteous Felon, 4505)","https://www.nosh.com/tag/meat-snacks/"),
      src("CB Insights","2026","New Primal","https://www.cbinsights.com/company/new-primal"),
      src("Archer","2025, April 30","New flavors, bigger reach","https://archerjerky.com/blogs/the-range/new-flavors-bigger-reach-archer-ignites-next-phase-of-explosive-growth"),
      src("Star Tribune","2021, May 25","Investors buy Mighty Spark","https://www.startribune.com/article/600060969"),
      src("Morrison Foerster","2026, January 8","New U.S. Dietary Guidelines released","https://www.mofo.com/resources/insights/260108-new-u-s-dietary-guidelines-released"),
      src("Food Ingredients First","2026","Dietary guidelines protein and processed foods","https://www.foodingredientsfirst.com/news/dietary-guidelines-protein-processed-foods.html"),
      src("Western Livestock Journal","2026","Updated Dietary Guidelines spotlight protein","https://www.wlj.net/updated-dietary-guidelines-spotlight-protein/"),
      src("The Poultry Site / Reuters","2026, April 2","Beyond Meat misses Q4 revenue on weak demand","https://www.thepoultrysite.com/news/2026/04/beyond-meat-misses-q4-revenue-on-weak-demand"),
      src("Just Food via Yahoo Finance","2026","Beyond Meat expects Q1 sales to be down again","https://finance.yahoo.com/markets/stocks/articles/beyond-meat-expects-q1-sales-120003413.html"),
      src("Newser / AP","2026, March 6","Beyond Meat drops the 'Meat'","https://www.newser.com/story/384912/beyond-meat-drops-the-meat.html"),
      src("Beef Central","2025","Beyond Meat continues to spiral downwards","https://www.beefcentral.com/?p=247366"),
      src("Food Dive","2026","Impossible Foods CEO Peter McGuinness steps down","https://www.fooddive.com/news/impossible-foods-ceo-steps-down-peter-mcguinness/811040/"),
      src("Agroempresario / 210 Analytics","2026","Refrigerated plant-based meat sales decline","https://agroempresario.com/publicacion/115371/impossible-foods-ceo-peter-mcguinness-steps-down-amid-pressure-on-the-plant-based-sector/"),
      src("Yahoo Finance","2025","GFI: plant-based meat sales down 7% in 2024","https://finance.yahoo.com/news/beyond-meat-cut-6-workforce-100000001.html"),
      src("Exploding Topics","2026","Beef organ supplement","https://explodingtopics.com/topic/beef-organ-supplement-6mmdhys6"),
      src("ASInsight","2026, July","Best-selling beef organs on Amazon","https://www.asinsight.com/report/US/beef-organs"),
    ])
    charts = dch + [lch,
      {"type":"lines","id":"chMeatIdx","start":2026,"end":2031,"legend":"lgMeat","series":[["Meat sticks, global (R&M)",0.0709,C['ink']],["Meat snacks, global (R&M)",0.0659,C['taupe']],["Plant-based meat, U.S. retail (GFI 2024 rate)",-0.07,C['mute'],1]]},
      {"type":"hbars","id":"chMeatShare","labelW":60,"labelWm":50,"max":60,"rows":[["2022",37.9,"37.9%",C['sand']],["2026",54.4,"54.4%",C['ink']]]},
      {"type":"hbars","id":"chMeatPB","labelW":60,"labelWm":50,"rows":[["2021",490,"~$490M",C['sand']],["2025",276,"$276M",C['ink']]]},
      {"type":"quadrant","id":"chMeatOpp","H":360,"xa":2,"xb":10,"ya":1,"yb":10,"quads":OPPQ,"xl":"Growth momentum →","xs":"Momentum →","yl":"Open space (fewer scaled players) →","ys":"Open space →",
       "points":[["Women's protein snacks",6.4,9.0,"r"],["Organ meat in new formats",5.4,7.8,"r"],["Better-for-you meat sticks",9.0,6.4,"l"],["Poultry and pork sticks",6.8,6.0,"r"],["GLP-1 portion protein",8.0,7.6,"l"],["Hybrid meat-plant blends",3.6,5.6,"r"],["Commodity jerky",4.0,2.6,"r"],["Private-label sticks",7.0,2.2,"r"],["Plant-based meat",2.6,1.6,"r"]]}]
    body = h + s + ctx + seg + rules + out + deals + land + funds + strat + vo + th + risks + srcs + pagenext(THESES[1], THESES[3])
    return body, charts

# ======================= WEARABLES =======================
def wear():
    col = '#9B72CF'
    h = hero("wear","Thesis: discreet wearables and women's health","Health tech you wear like jewelry",
        "Women are already the core customer of the smart ring. The next wave makes health tracking disappear into what women already wear: slimmer rings, ring covers and jackets, smart earrings, and the women's health software and care partnerships that turn data into answers.",
        [("Lumia","Untapped","Smart earrings tracking blood flow, sleep, and cycle; $7M raised."),
         ("Incora Health","Untapped","Fertility-focused earring with a completed clinical trial at seed."),
         ("Mira","Breakout","At-home hormone testing now integrated into Oura."),
         ("Ultrahuman","Breakout","Subscription-free ring; $70M raise as U.S. demand outran supply."),
         ("Steff Eleoff","Untapped","Handcrafted fine-jewelry covers built on Oura's installed base.")],
        [("72%","of Oura's members are women, per its IPO filing"),("$1.21B","Oura revenue in the nine months to June 2026, up 74%"),("5.7M","Oura paid members at the end of fiscal 2026"),("$1.55B","record women's health equity raised in 2025 (W Group)")], col)
    s = summary([
        ("Customer","Women are the core smart ring buyer","72% of Oura's members are women, and more than half report a chronic condition.","context","Why now"),
        ("Scale","Oura proved the business","Profitable, guiding to 90% growth, and valued at about $11B privately.","deals","Deal flow"),
        ("Form factor","Rings got slimmer; earrings are next","Lumia and Incora are building earrings; ear placement reads temperature well.","segments","Category map"),
        ("Policy","FDA opened the wellness door","January 2026 guidance lets non-invasive wellness wearables estimate blood pressure and more.","rules","Regulation"),
        ("Thesis","Build around the ring, not against it","Jewelry layers, new form factors, and women's health insights ride an installed base.","thesis","Investment thesis"),
        ("Risks","Patents, accuracy, and privacy","ITC fights and an accuracy class action show the hardware risks.","risks","Key risks")])
    ctx = section("context","Why now","The wrist was built for workouts. Women want tracking that fits a ring stack, an ear, and a cycle.",
      '<div class="two"><div class="callout"><h3>Oura is a women\'s health company in disguise</h3><p>Oura\'s S-1 showed about 72% of members are women and more than half report at least one chronic condition. It has added cycle, pregnancy, perimenopause, and birth control features, plus a women\'s health AI model launched in February 2026.</p><p>Partnerships with Maven Clinic, Midi Health, Mira, Progyny, and Dexcom turn the ring into a front door to care.</p></div>'
      '<div class="callout"><h3>Form factor is the product</h3><p>Oura launched Ring 5, its slimmest yet, and ceramic editions marketed as fashion first. A cottage industry of covers, jackets, and stacking rings followed, from Amazon multipacks to a handmade diamond Cover Ring from Milan.</p><p>Earrings are the next frontier. University of Washington researchers found the earlobe is a strong spot to read skin temperature, which matters for ovulation tracking.</p></div></div>'
      + cards([("Underfunded but rising","Women\'s health drew a record $1.55B of equity in 2025, yet the WEF and BCG say it still gets only about 6% of private healthcare investment."),
               ("AI raises valuations","SVB finds AI-enabled women\'s health startups command a median $35M pre-money, about triple their non-AI peers."),
               ("Subscription models stick","Oura reported about 85% 12-month paid member retention, the benchmark for any new device.")]))
    seg = section("segments","Category map","The opportunity sits around and beyond the ring.",
      '<div class="controls" role="group" aria-label="Filter segments"><button class="flt" data-g="seg" data-f="all" aria-pressed="true">All</button><button class="flt" data-g="seg" data-f="early" aria-pressed="false">Early-stage friendly</button><button class="flt" data-g="seg" data-f="scaled" aria-pressed="false">Scaled</button></div>' +
      table(["Segment","What it is","Leaders","Signal","Watch-outs"],[
        ["<strong>Smart rings</strong>","Finger-worn sensors for sleep, recovery, temperature, cycle","Oura, Ultrahuman, Samsung, Circular","Oura FY2025 revenue $907.9M; ~85% U.S. share in late 2025","Patent wars; capital-intensive hardware"],
        ["<strong>Smart earrings</strong>","Earring-based sensors for temperature, blood flow, cycle","Lumia, Incora Health, Zura Health","Lumia raised $7M; Incora ran a clinical trial at seed","Battery, sizing, and proving accuracy"],
        ["<strong>Ring accessories and jewelry</strong>","Covers, jackets, and stackers that turn a ring into jewelry","Steff Eleoff, LIL Milan, Bille Simone, OSleeve","Fine jewelers entering; fashion press coverage","Dependence on Oura's design; fit changes each generation"],
        ["<strong>Women's health platforms</strong>","Hormone testing, menopause care, virtual clinics","Mira, Midi Health, Maven Clinic","Midi raised $50M Series C; Oura integrations","Reimbursement and clinical scaling"],
        ["<strong>Women-first rings</strong>","Rings designed and tuned for women","Movano Evie","Proved demand for women-specific design","Distribution and scale proved hard"]], 860, fg="seg",
        tags=["scaled","early","early","early scaled","early"]))
    rules = section("rules","Regulation","The FDA just widened what a wellness wearable can say, which lowers the bar for new devices.",
      '<div class="two"><div><h3>FDA timeline</h3><ul class="tl">'
      '<li><b>2025</b>FDA said products estimating blood pressure were not low-risk wellness products.</li>'
      '<li><b>January 6, 2026</b>Revised General Wellness guidance: non-invasive wearables may estimate blood pressure, oxygen saturation, glucose, and HRV as wellness outputs if they avoid diagnosis.</li>'
      '<li><b>January 23, 2026</b>Draft guidance set clinical testing expectations for cuffless blood pressure devices that do make medical claims.</li></ul>'
      '<p class="note">Why it matters: earrings and rings can ship wellness features faster, but anything that diagnoses still needs clearance.</p></div>'
      '<div><div class="callout"><h3>Patent wars decide who can sell</h3><p>Oura\'s ITC case kept Ultrahuman\'s Ring Air out of the U.S. for months in 2025, leaving Oura with about 85% of U.S. smart ring share. Several rivals still face possible import bans.</p></div>'
      '<div class="callout"><h3>Accuracy and privacy</h3><p>Users filed a class action in August 2026 alleging Oura cannot accurately measure sleep cycles. Reproductive health data is among the most sensitive data a company can hold.</p></div></div></div>')
    out = section("outlook","Market and outlook","The ring category is small in dollars but compounding fast, and one company shows what scale looks like.",
      '<div class="chartgrid">' + figure("chWearIdx","Projected smart ring market growth, 2025 = 100","Global smart rings, $417.5M in 2025, at Grand View Research's 22.5% CAGR, compared with the broader U.S. supplement market for scale of pace.", '<div class="legend" id="lgWear"></div>', wide=True)
      + figure("chOura","Oura revenue by fiscal year","FY2024 and FY2025 from the S-1; FY2026 applies the company's guided ~90% growth.")
      + figure("chFem","Women's health venture investment","SVB, U.S. and Europe. 2025 dipped from the 2024 peak; SVB expects a rebound in 2026.")
      + figure("chWearOpp","Opportunity map","Author's assessment of momentum against open space. Qualitative.", wide=True) + '</div>'
      + cards([("Fastest growth: rings","Smart rings are forecast to grow about 22.5% a year through 2033."),("Biggest pool: the platform","Oura alone did $1.21B in nine months; membership revenue grew 121%."),("Most open: earrings and jewelry","Earrings and fine-jewelry layers have pull from women and almost no scaled players.")]))
    deals, dch = deals_section("wear","Ring makers and women's health platforms set the comps; earrings are where early rounds are happening.")
    land, lch = landscape_section("Wearables", [
      ["Lumia",3.4,8.6,"r",7,"w"],["Incora Health",1.4,7.8,"r",0.5,"w"],["Steff Eleoff",2.4,6.6,"r",0,"w"],["Mira",4.4,7.1,"r",0,"w"],["Ultrahuman",6.6,6.9,"r",70,"w"],
      ["Zura Health",1.2,4.2,"r",0,"e"],["LIL Milan",3.4,4.6,"r",0,"e"],["OSleeve",2.0,3.0,"r",0,"e"],["Midi Health",6.0,5.7,"r",50,"e"],["Circular",4.4,3.4,"r",0,"e"],
      ["Movano Evie",3.0,1.6,"r",0,"d"],["Maven Clinic",8.0,4.2,"l",420,"i"],["Oura",9.4,3.2,"l",1500,"i"],["Samsung Galaxy Ring",8.6,1.4,"l",0,"i"],["WHOOP",7.0,2.4,"l",575,"i"]])
    funds = section("funds","Who's already writing checks","Late-stage capital crowned Oura; a new set of women's health funds is forming underneath it.",
      cards([("Fidelity","Led Oura's $900M+ round at about $11B and its 2024 Series D at $5.2B."),
             ("Forerunner Ventures","Early Oura backer led by Kirsten Green; held about 9.3% and planned to sell its full stake in the IPO."),
             ("Dexcom","Strategic investor in Oura and a glucose data partner."),
             ("Nina Capital, Bread & Butter, GG Ventures","Among 11 new women's health funds that emerged in 2025, per W Group."),
             ("Bootstrapped jewelers","Steff Eleoff and LIL Milan are founder-owned today, an opening for small consumer checks."),
             ("Hardware crowdfunding","Lumia ran a crowdfunding launch for Lumia 2 alongside its $7M raise, a common path for jewelry tech.")]))
    strat = section("strategics","What the big players are doing","Big tech is bundling rings into ecosystems; care platforms are plugging into them.",
      cards([("Oura","Building a women's health platform: cycle, pregnancy, perimenopause, and a women's health AI model."),
             ("Samsung","Galaxy Ring at $399 with no subscription; Ring 2 likely pushed to 2027 amid patent disputes."),
             ("Maven Clinic and Midi Health","Care partners that turn ring data into virtual visits and treatment."),
             ("Mira and Progyny","Hormone and fertility partners integrating with Oura."),
             ("Dexcom","Connects glucose data with ring insights through its Stelo product."),
             ("Fine jewelers","LIL Milan and independent designers are building jewelry for smart rings.")]))
    vo = section("voices","Who's shaping the conversation", None, voices([
      ("Said Oura has “the luxury of choosing our moment” after postponing its IPO.","Tom Hale","CEO, Oura",0),
      ("Says the best smart ring is simply the one people actually want to wear.","Miklu Silvanto","Chief Design Officer, Oura",0),
      ("“Just as Oura made rings smart, we've made earrings smart.”","Lumia","Smart earring startup, Boston",0),
      ("Points out women's health is treated as niche though it covers half the population.","Theresa Gevaert","Co-founder, Incora Health",0),
      ("Argues women's health is no longer an emerging category seeking validation.","W Group","Global women's health investment report",0),
      ("Said the big concern about Oura going public is valuation.","Jay Ritter","Director, IPO Initiative, University of Florida",1)]))
    th = thesis_section("The next billion-dollar health wearable will be worn like jewelry. Women are already the core customer, and they will pay for devices that disappear into what they already wear and for insights built on female physiology. The early-stage opportunity sits around the ring: new form factors, the jewelry layer, and women's health software and care that turn data into answers.",
      [("New form factors","Earrings read temperature well and fit how women already dress."),
       ("The jewelry layer","Covers and jackets ride Oura's 5.7M members with fashion margins and little R&D."),
       ("Cycle to menopause insights","Female physiology is the data moat most wearables still ignore."),
       ("Care partnerships as distribution","Oura plus Maven, Midi, and Mira shows how devices reach patients."),
       ("A friendlier FDA","January 2026 guidance lets wellness devices show more metrics without clearance."),
       ("Subscription-free challengers","Ultrahuman and Samsung pressure Oura's membership model from below.")],
      ["Validation against clinical gold standards","12-month retention (Oura's ~85% is the bar)","Subscription attach rate","Design and fashion credibility","Female physiology datasets","Data privacy posture","Freedom to operate on patents"],
      ["Me-too rings exposed to ITC import bans","Hardware with no software or data moat","Devices edging into diagnosis without clearance"],
      "Smart earrings and pendants built for cycle and perimenopause tracking. Fine-jewelry and fashion brands designed around the major rings. Software that turns ring data into fertility, menopause, and cardiometabolic guidance for women. Care partnerships where a device is the entry point.")
    risks = risks_section([
      ("Patent litigation","Oura's ITC wins kept rivals out of the U.S.; several rings still face bans.","Freedom-to-operate work and licensing before launch"),
      ("Accuracy claims","An August 2026 class action alleges Oura misreads sleep cycles.","Published validation and conservative marketing"),
      ("Reproductive data privacy","Cycle and fertility data is highly sensitive.","On-device processing, minimal data retention, clear consent"),
      ("Hardware economics","Hardware was 80% of Oura's revenue in the first nine months of fiscal 2026.","Subscription revenue and partnerships"),
      ("Platform bundling","Samsung and Apple can bundle health tracking into phones and watches.","Women-specific features and design the giants won't prioritize"),
      ("Funding volatility","Deloitte counted a 56% drop in narrowly defined women's health tech funding in 2025, even as broader trackers hit records.","Clinical proof and revenue before large raises")])
    srcs = sources_section([
      src("the5krunner","2026, September 4","Oura IPO: revenue declared up 74%","https://the5krunner.com/2026/09/04/oura-ipo-s1-revenue/"),
      src("Renaissance Capital","2026, September 3","Smart ring maker Oura files for an estimated $2.5 billion IPO","https://www.renaissancecapital.com/IPO-Center/News/121478/Smart-ring-maker-Oura-files-for-an-estimated-$2.5-billion-IPO"),
      src("Pulse 2.0 / Reuters","2026, September 22","Oura seeks up to $2.2 billion at $15.6 billion IPO valuation","https://pulse2.com/oura-seeks-up-to-2-2-billion-at-15-6-billion-ipo-valuation/"),
      src("Healthcare Dive","2026, September 29","Oura delays IPO","https://www.healthcaredive.com/news/oura-delays-ipo/831655/"),
      src("TechCrunch","2026","Oura shelves its $2.2B IPO","https://techcrunch.com/?p=3171207"),
      src("IFR","2026, October 3","Oura pulls US$2.2bn IPO over valuation and lockup","https://www.ifre.com/equities/2493350/smart-ring-maker-oura-pulls-us2.2bn-ipo-over-valuation-and-lockup"),
      src("MD+DI","2026, September 29","Oura's IPO: a case of cold feet?","https://www.mddionline.com/wearable-medical-devices/oura-s-ipo-a-case-of-cold-feet-"),
      src("MobiHealthNews","2026","Oura confidentially files for IPO","https://www.mobihealthnews.com/news/oura-confidentially-files-ipo-revenue-growth-soars"),
      src("MD+DI","2026, May 22","Oura quietly plans to go public","https://www.mddionline.com/wearable-medical-devices/oura-quietly-plans-to-go-public"),
      src("TechCrunch","2026, September","The smart ring market is getting crowded","https://techcrunch.com/?p=3160959"),
      src("Sacra","2026","Ultrahuman","https://sacra.com/c/ultrahuman"),
      src("Grand View Research via GII","2026","Smart rings market size report","https://m.giikorea.co.kr/report/grvi1942015-smart-rings-market-size-share-trends-analysis.html"),
      src("iDevice","2026","Smart ring buyers guide 2026","https://idevice.com/smart-ring-buyers-guide-2026-oura-samsung-ultrahuman-circula-1ea4e781"),
      src("Athletech News","2025, November 18","Lumia raises $7M, launches blood-flow tracking smart earrings","https://athletechnews.com/lumia-raises-7-million-blood-flow-tracking-smart-earrings/"),
      src("Femtech Insider","2025","Smart earrings for fertility tracking: Incora Health","https://femtechinsider.com/smart-earrings-for-fertility-tracking-incora-health-prepares-for-market-debut/"),
      src("Dealroom","2026","Incora Health","https://app.dealroom.co/companies/incora_health"),
      src("Munich Startup","2026, August 28","Zura Health: more than just another fitness tracker","https://www.munich-startup.de/en/news/zura-health-more-than-just-another-fitness-tracker"),
      src("University Hospitals","2026, May","Smart earrings: the next big thing in wearables?","https://www.uhhospitals.org/blog/articles/2026/05/smart-earrings"),
      src("Inquirer Technology","2024, March 4","Scientists make health-tracking smart earrings","https://technology.inquirer.net/?p=132527"),
      src("NBC Select","2026","Accessorize your Oura Ring with covers, jackets and sleeves","https://www.nbcnews.com/select/shopping/oura-ring-jackets-sleeves-covers-accessories-rcna259350"),
      src("Grazia","2026","The best Oura ring covers","https://graziadaily.co.uk/beauty-hair/wellness/best-oura-ring-covers/"),
      src("JCK","2025, November 17","LIL Milan presents LIL Cover Ring","https://lasvegas.jckonline.com/en-us/media/press-releases/lil-milan-presents-lil-cover-ring.html"),
      src("Fast Company","2025, October 2","Oura's latest smart rings hope technology can blend with fashion","https://fastcompany.co.za/co-design/2025-10-02-ouras-latest-smart-rings-hope-technology-can-blend-with-fashion"),
      src("Oura","2026","New FDA guidance","https://ouraring.com/blog/fr/new-fda-guidance/"),
      src("Ropes & Gray","2026, January","FDA updated guidances on general wellness products","https://www.ropesgray.com/en/insights/alerts/2026/01/fda-adapts-with-the-times-on-digital-health-updated-guidances-on-general-wellness-products"),
      src("Hardian Health","2026","Blood pressure, wearables, and FDA General Wellness Guidance","https://www.hardianhealth.com/insights/fda-wearables-guidelines-update-2026"),
      src("SVB","2026","Innovation in Women's Health","https://www.svb.com/trends-insights/reports/womens-health-report/"),
      src("Fierce Healthcare","2026","Women's health equity funding hits new high","https://www.fiercehealthcare.com/ai-and-machine-learning/w-group-releases-1st-global-womens-health-investment-report-tracking-record"),
      src("Pharmaceutical Technology","2026","Women's health attracted record equity in 2025","https://www.pharmaceutical-technology.com/news/womens-health-attracted-record-equity-in-2025-as-companies-share-capital/"),
      src("Mean CEO","2026","Femtech startup funding statistics","https://blog.mean.ceo/?p=5755"),
      src("TechCrunch","2023","Movano on why its health wearable will put women first","https://techcrunch.com/?p=2476444"),
    ])
    charts = dch + [lch,
      {"type":"lines","id":"chWearIdx","start":2025,"end":2033,"legend":"lgWear","series":[["Smart rings, global (Grand View)",0.225,C['ink']],["U.S. supplements, for comparison (NBJ)",0.0597,C['mute'],1]]},
      {"type":"hbars","id":"chOura","labelW":120,"labelWm":104,"rows":[["FY2024",406.8,"$406.8M",C['sand']],["FY2025",907.9,"$907.9M",C['sand']],["FY2026 (guided)",1725,"~$1.7B",C['ink']]]},
      {"type":"hbars","id":"chFem","labelW":60,"labelWm":50,"rows":[["2024",2600,"$2.6B",C['sand']],["2025",2000,"$2.0B",C['ink']]]},
      {"type":"quadrant","id":"chWearOpp","H":360,"xa":2,"xb":10,"ya":1,"yb":10,"quads":OPPQ,"xl":"Growth momentum →","xs":"Momentum →","yl":"Open space (fewer scaled players) →","ys":"Open space →",
       "points":[["Smart earrings",6.0,8.8,"r"],["Ring jewelry and covers",7.6,7.6,"l"],["Cycle and menopause insights",8.8,6.4,"l"],["Care partnerships",6.6,5.6,"r"],["Pendants and other jewelry",5.2,7.0,"r"],["Generic smart rings",8.8,2.4,"l"],["Subscription-free rings",6.2,3.6,"r"],["Diagnosis-grade claims",3.2,4.0,"r"],["Wrist trackers",4.0,1.6,"r"]]}]
    body = h + s + ctx + seg + rules + out + deals + land + funds + strat + vo + th + risks + srcs + pagenext(THESES[2], None)
    return body, charts
