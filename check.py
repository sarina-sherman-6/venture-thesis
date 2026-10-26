"""Sanity checks the weekly agent runs before committing. Exits 1 on any problem."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import COMPANIES, DEALS
errs = []
seen = {}
for c in COMPANIES:
    if c["slug"] in seen: errs.append(f"duplicate company: {c['name']}")
    seen[c["slug"]] = c
    if c["thesis"] not in ("fiber", "nonalc", "meat", "wear"): errs.append(f"bad thesis on {c['name']}")
    if "latest" in c and not re.fullmatch(r"\d{4}(-\d{2})?", str(c["latest"])): errs.append(f"bad latest date on {c['name']}: {c['latest']}")
for t, ds in DEALS.items():
    keys = []
    for d in ds:
        if len(d) != 9: errs.append(f"{t}: deal tuple needs 9 fields: {d[:3]}"); continue
        if not re.fullmatch(r"\d{4}-\d{2}", d[0]): errs.append(f"{t}: bad date key {d[0]}")
        if d[7] not in ("r", "e", "s"): errs.append(f"{t}: kind must be r/e/s on {d[2]}")
        if d[8] is not None and not isinstance(d[8], (int, float)): errs.append(f"{t}: size must be a number or None on {d[2]}")
        keys.append((d[0], d[2]))
    if len(keys) != len(set(keys)): errs.append(f"{t}: duplicate deal")
txt = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.py"), encoding="utf-8").read() + open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fiber_rows.json"), encoding="utf-8").read()
if "—" in txt: errs.append("em dash found in data; use commas, colons, or parentheses")
print("\n".join(errs) or f"ok: {len(COMPANIES)} companies, {sum(len(v) for v in DEALS.values())} deals")
sys.exit(1 if errs else 0)
