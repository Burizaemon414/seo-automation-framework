from .config import Config
from .warehouse import Warehouse
from .common import setup_logging
import pandas as pd
from datetime import date, timedelta

def run():
    log = setup_logging()
    cfg = Config()
    wh = Warehouse(cfg.warehouse_path)

    log.info("Simulating GSC pull... (replace with real API calls)")
    today = date.today()
    rows = []
    for i in range(7):
        rows.append({
            "date": (today - timedelta(days=i)).isoformat(),
            "page": "/blog/nextjs-seo",
            "query": "nextjs seo",
            "country": "THA",
            "device": "desktop",
            "clicks": 10 + i,
            "impressions": 200 + i*5,
            "ctr": (10+i)/(200+i*5),
            "position": 7 - i*0.1
        })
    df = pd.DataFrame(rows)
    wh.write_df(df, "gsc_daily")
    log.info("Wrote %d rows to gsc_daily in %s", len(df), cfg.warehouse_path)

if __name__ == "__main__":
    run()
