# SEO Automation Code (Proflow Labs)

This bundle contains runnable stubs and utilities to automate the SEO data flows
described in `seo_automation_config.yaml`. The scripts are dependency-light and
safe to run locally or in CI. Real API calls are left as TODOs with clear hooks.

## Contents
- `seo_automation/config.py` — Load YAML config with helpful getters
- `seo_automation/warehouse.py` — Simple DuckDB warehouse helper (file-based)
- `seo_automation/gsc_pull.py` — Stub to pull Search Console data (prints schema & writes demo table)
- `seo_automation/cwvs_collect.py` — Stub to collect PageSpeed CWV metrics for URLs
- `seo_automation/serp_scan.py` — Stub to query SERP provider & store features
- `seo_automation/keyword_refresh.py` — Stub to refresh CPC/KD/volatility
- `seo_automation/strapi_sync.py` — Stub to validate Strapi SEO fields & suggest links
- `seo_automation/generate_content_plan.py` — Reads Excel Master_Priority and exports Top-N CSV
- `.github/workflows/seo_automation.yml` — GitHub Actions with cron & manual dispatch
- `Makefile` — Local developer commands

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export CONFIG=/mnt/data/seo_automation_config.yaml  # or path in repo
python -m seo_automation.generate_content_plan --excel /mnt/data/SEO_Intelligence_v2.xlsx --out out/content_plan.csv --top 50
```

## Notes
- Replace TODO blocks with real API calls (GSC, GA4, SERP, PageSpeed, Strapi).
- DuckDB is used by default for a portable warehouse: `warehouse/seo.duckdb`.
