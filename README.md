# Sarina's Venture Thesis

Consumer venture research across four theses: fiber, non-alc, meat protein, and discreet wearables for women's health.

- `data.py` and `fiber_rows.json`: every company and deal on the site
- `lib.py`, `pages_new.py`, `build.py`: page templates and the site generator
- `assets/`: styles and charts
- `docs/`: the built site that GitHub Pages serves (do not edit by hand)
- `AGENT.md`: instructions for the weekly deal-update agent
- `check.py`: data checks run before every update

To rebuild after editing data: `python3 check.py && python3 build.py`
