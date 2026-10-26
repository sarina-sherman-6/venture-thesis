# Weekly deal-update playbook

This file is the instruction set for the scheduled agent that keeps Sarina's Venture Thesis current. Follow it exactly. Never use em dashes anywhere (data, commit messages, PR text).

## What counts as a new deal

A funding round, acquisition, IPO, or major strategic investment announced in the last 10 days that fits one of the four theses:

| Thesis key | Thesis | In scope |
|---|---|---|
| `fiber` | Fiber and gut health | Fiber and prebiotic brands, fiber ingredients, gut testing, GLP-1 nutrition support |
| `nonalc` | Non-alc and moderation | Non-alcoholic beer, wine, spirits, functional tonics, hemp and THC drinks, moderation platforms |
| `meat` | Meat protein | Meat sticks, jerky, organ meat supplements, regenerative meat brands, plus notable plant-based meat shutdowns or down rounds |
| `wear` | Discreet wearables and women's health | Smart rings and earrings, ring accessories, femtech devices, cycle and fertility tracking, menopause tech |

Skip: rumors, unconfirmed reports, deals already in `data.py`, and companies outside these four lanes.

## Where to look

1. **SEC Form D filings.** Check recent Form D filings on SEC EDGAR full-text search (efts.sec.gov/LATEST/search-index?q=...&forms=D, or www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=D) for companies already in `data.py` and for thesis keywords (prebiotic, fiber, non-alcoholic, adaptogen, meat stick, jerky, smart ring, wearable, fertility, menopause). A Form D gives the amount sold and the date, often before press coverage. Use the "total amount sold" as the raise size.
2. **Web search.** Search the web for each thesis with the current month and year, for example "prebiotic fiber brand raises Series A October 2026". Good sources: company press releases, BevNET, Food Dive, Food Navigator, TechCrunch, Axios Pro, Crunchbase News, Fierce Healthcare, FemTech Insider. If the PitchBook connector is available, use it to confirm amounts and investors. Every deal you add needs at least one source URL you actually opened.

## How to add a deal

1. **Deal row.** In `data.py`, add a tuple to the right list in `DEALS`, keeping newest first:
   `("YYYY-MM", "Mon YYYY", "Company", "what they do, short", "deal text e.g. $12M Series A", "lead (lead), other investors", "one-line VC read-through", kind, size)`
   `kind` is `"r"` raise, `"e"` exit or acquisition, `"s"` strategic. `size` is the dollar amount in millions as a number, or `None` if undisclosed.
2. **Company row.** If the company is already in the database, update its `latest` (YYYY-MM), `latestNote`, `investors`, `raisedM`, and `status`. If it is new:
   - Non-alc, meat, and wearables companies go in the matching `rows(...)` list in `data.py`, in the field order `name, category, what, investors, why, watch(0/1), status, raisedM, raisedPlus(0/1), latest, latestNote`. Reuse a category that already exists in that thesis.
   - Fiber companies go in `fiber_rows.json` with the same field names.
   - Set `watch` to 0. Sarina decides what goes on the watch list.
3. **Date stamp.** In `lib.py`, set `UPDATED` to today's date, e.g. `"October 26, 2026"`.

Do not change page copy, charts, theses, colors, or layout. Only data.

## Build, check, and ship

```bash
python3 check.py      # must print ok
python3 build.py      # must print ok and rewrite docs/
```

Then create a branch `deals/YYYY-MM-DD`, commit (`Add N deals: Company A, Company B`), push, and open a pull request to `main`. The PR description lists each deal with its thesis, amount, investors, and source links, then anything you found but skipped and why. If nothing new qualified, do not open a PR; just report "No new deals this week" with what you searched.
