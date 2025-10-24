from .config import Config
from .warehouse import Warehouse
from .common import setup_logging
import pandas as pd

REQUIRED_SEO_FIELDS = ["title", "meta_title", "meta_description", "slug"]

def run():
    log = setup_logging()
    cfg = Config()
    wh = Warehouse(cfg.warehouse_path)

    log.info("Simulating Strapi sync & SEO validation... (replace with Strapi API)")
    # Demo entries
    entries = [
        {"id": 1, "title": "Next.js SEO Basics", "meta_title": "Next.js SEO Basics", "meta_description": "Guide", "slug": "nextjs-seo-basics", "status": "draft"},
        {"id": 2, "title": "Strapi SEO Setup", "meta_title": "", "meta_description": "Config", "slug": "strapi-seo-setup", "status": "draft"},
    ]
    df = pd.DataFrame(entries)
    # Validation
    for f in REQUIRED_SEO_FIELDS:
        df[f"{f}_ok"] = df[f].astype(str).str.len() > 0
    df["seo_ready"] = df[[f"{f}_ok" for f in REQUIRED_SEO_FIELDS]].all(axis=1)

    wh.write_df(df, "strapi_entries")
    log.info("Validated %d entries; %d ready", len(df), int(df["seo_ready"].sum()))

if __name__ == "__main__":
    run()
