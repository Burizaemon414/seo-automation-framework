from .config import Config
from .warehouse import Warehouse
from .common import setup_logging
import pandas as pd

def run():
    log = setup_logging()
    cfg = Config()
    wh = Warehouse(cfg.warehouse_path)

    log.info("Simulating keyword metrics refresh... (replace with CPC/KD provider)")
    rows = [
        {"keyword": "nextjs seo", "cpc": 2.4, "kd": 38, "volatility": 0.31},
        {"keyword": "strapi seo", "cpc": 1.8, "kd": 32, "volatility": 0.28},
    ]
    df = pd.DataFrame(rows)
    wh.write_df(df, "keywords_universe")
    log.info("Updated keyword metrics (demo)")

if __name__ == "__main__":
    run()
