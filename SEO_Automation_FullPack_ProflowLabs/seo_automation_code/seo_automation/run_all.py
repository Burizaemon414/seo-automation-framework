from . import gsc_pull, cwvs_collect, serp_scan, keyword_refresh, strapi_sync
from .common import setup_logging

def run_all():
    log = setup_logging()
    log.info("Running all demo pipelines sequentially...")
    gsc_pull.run()
    cwvs_collect.run()
    serp_scan.run()
    keyword_refresh.run()
    strapi_sync.run()
    log.info("All demo pipelines completed.")

if __name__ == "__main__":
    run_all()
