# RUNBOOK

## Daily
1. `gsc_pull` — fetch last N days GSC and append to warehouse.
2. `cwvs_collect` — fetch PageSpeed CWV metrics for canonical URLs.
3. `serp_scan` — capture SERP top-10 and features for priority keywords.

## Weekly
1. `keyword_refresh` — refresh CPC/KD/volatility.
2. `strapi_sync` — validate SEO fields, suggest internal links.

## Export
- `generate_content_plan` reads `SEO_Intelligence_v2.xlsx:Master_Priority` and exports Top-N rows to `out/content_plan.csv`.
