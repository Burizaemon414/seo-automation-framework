from .config import Config
from .warehouse import Warehouse
from .common import setup_logging
import pandas as pd, random

def run():
    log = setup_logging()
    cfg = Config()
    wh = Warehouse(cfg.warehouse_path)

    log.info("Simulating CWV collection... (replace with PageSpeed API calls)")
    urls = ["/", "/blog/nextjs-seo", "/blog/strapi-seo"]
    rows = []
    for u in urls:
        rows.append({
            "url": u,
            "strategy": "mobile",
            "lcp_ms": random.randint(1500, 3500),
            "cls": round(random.uniform(0.01, 0.25), 3),
            "inp_ms": random.randint(120, 280)
        })
    df = pd.DataFrame(rows)
    wh.write_df(df, "cwvs_history")
    log.info("Wrote %d rows to cwvs_history", len(df))

if __name__ == "__main__":
    run()
