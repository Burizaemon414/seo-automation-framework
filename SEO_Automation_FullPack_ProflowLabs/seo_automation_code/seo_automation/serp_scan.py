from .config import Config
from .warehouse import Warehouse
from .common import setup_logging
import pandas as pd

def run():
    log = setup_logging()
    cfg = Config()
    wh = Warehouse(cfg.warehouse_path)

    log.info("Simulating SERP scan... (replace with real SERP provider)")
    rows = [
        {"keyword": "nextjs seo", "position": 5, "feature": "sitelinks", "timestamp": "now"},
        {"keyword": "strapi seo", "position": 9, "feature": "people_also_ask", "timestamp": "now"},
    ]
    df = pd.DataFrame(rows)
    wh.write_df(df, "serp_features")
    log.info("Wrote SERP features to warehouse")

if __name__ == "__main__":
    run()
