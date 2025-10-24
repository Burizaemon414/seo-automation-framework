# FORMULAS

- **Traffic Potential** = `search_volume * est_ctr * cps`
- **Keyword Value** = `IF(CVR & AOV > 0) traffic_potential * cvr * aov ELSE cpc * traffic_potential`
- **Difficulty Index** = `KD*0.5 + PPC*0.2 + CompetitorDA*0.2 + (Volatility*100)*0.1`
- **Comp Index** = `(difficulty_index + cpc*10)/2`
- **Opportunity Score** = `keyword_value / (comp_index + 1)`
- **Strategic Fit** = `(AVERAGE(brand_relevance, topical_fit, intent_match, ilp)/5)*80 + serp_feature_ownership*0.2`
- **Master Priority** = `0.25*Demand + 0.25*Value + 0.20*Opportunity + 0.15*CompetitionEase + 0.15*StrategicFit`
- **Normalization (0–100)** = `(x - MIN) / (MAX - MIN) * 100` (guard DIV/0)
