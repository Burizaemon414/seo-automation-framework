FROM python:3.11-slim
WORKDIR /app
COPY seo_automation_code/ ./seo_automation_code/
COPY docs/ ./docs/
RUN pip install --no-cache-dir -r seo_automation_code/requirements.txt
ENV CONFIG=/app/docs/seo_automation_config.yaml
CMD ["python", "-m", "seo_automation.run_all"]
