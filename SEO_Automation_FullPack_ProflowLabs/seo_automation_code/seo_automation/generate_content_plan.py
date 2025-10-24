import pandas as pd, argparse, os
from .common import setup_logging

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--excel", required=True, help="Path to SEO_Intelligence_v2.xlsx")
    parser.add_argument("--out", default="out/content_plan.csv")
    parser.add_argument("--top", type=int, default=50)
    args = parser.parse_args()

    log = setup_logging()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    xl = pd.ExcelFile(args.excel)
    mp = xl.parse("Master_Priority")
    cols = ["keyword","master_priority","demand_score","value_score","opportunity_score_pct","competition_ease_score","strategic_fit_score"]
    cols = [c for c in cols if c in mp.columns]
    topn = mp.sort_values("master_priority", ascending=False).head(args.top)[cols]
    topn.to_csv(args.out, index=False)
    log.info("Exported Top-%d content plan to %s", args.top, args.out)

if __name__ == "__main__":
    main()
