# Deploy Notes

## GitHub Actions
- Workflow: `.github/workflows/seo_automation.yml`
- Set repo **Secrets** for API keys (SERP, PageSpeed, etc.)

## Local Dev
```
python -m venv .venv && source .venv/bin/activate
pip install -r seo_automation_code/requirements.txt
export CONFIG=docs/seo_automation_config.yaml
python -m seo_automation.run_all
python -m seo_automation.generate_content_plan --excel docs/SEO_Intelligence_v2.xlsx --out out/content_plan.csv --top 50
```
