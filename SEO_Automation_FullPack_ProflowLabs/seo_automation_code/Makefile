PY=python
CONFIG?=/mnt/data/seo_automation_config.yaml
export CONFIG

install:
	$(PY) -m pip install --upgrade pip
	pip install -r seo_automation_code/requirements.txt

run-all:
	$(PY) -m seo_automation.run_all

content-plan:
	$(PY) -m seo_automation.generate_content_plan --excel /mnt/data/SEO_Intelligence_v2.xlsx --out out/content_plan.csv --top 50
