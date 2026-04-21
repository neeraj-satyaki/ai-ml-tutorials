# Data Science + Data Analytics + Storytelling

End-to-end view. Pipeline → analytics types → tools → storytelling.

## Pipeline — `Pipeline/`
How a real DS project flows.
- **ProblemFraming** — what decision does this inform? What is the cost of being wrong?
- **DataCollection** — sources, logging, scraping, surveys, APIs, sampling bias.
- **DataCleaning** — missing values, duplicates, outliers, dtype fixes, unit normalization.
- **EDA** — summary stats, distributions, correlations, pairplots, anomalies.
- **FeatureEngineering** — scaling, encoding (one-hot, target, embeddings), interactions, binning, time-based features.
- **Modeling** — baseline → complex. Cross-validate. Prevent leakage.
- **Evaluation** — right metric for problem (AUC vs F1 vs MAPE vs calibration); sliced by segment.
- **Deployment** — batch vs online; REST, streaming; containerize; feature store.
- **Monitoring** — data drift, concept drift, label delay, alerting, retraining triggers.

## Analytics Types — `Analytics/`
- **Descriptive** — what happened? (dashboards, KPIs, aggregations)
- **Diagnostic** — why did it happen? (drill-down, root cause, correlation, slicing)
- **Predictive** — what will happen? (forecasting, classification, regression)
- **Prescriptive** — what should we do? (optimization, simulation, policy)
- **TimeSeries** — trend, seasonality, stationarity, ARIMA, Prophet, state-space, transformers.
- **ABTesting** — hypothesis, power, CUPED, sequential testing, guardrail metrics.
- **CausalInference** — DAGs, confounders, IV, diff-in-diff, propensity scores, synthetic control, do-calculus.
- **Cohort** — group by signup date/segment, track retention over time.
- **Funnel** — stepwise conversion; find drop-off points.

## Tools — `Tools/`
- **SQL** — window funcs, CTEs, joins, aggregation; the lingua franca.
- **Pandas** — DataFrame wrangling; groupby, merge, pivot, apply.
- **NumPy** — vectorized arrays; foundation.
- **Spark** — distributed DF/SQL for big data; PySpark.
- **dbt** — SQL-based transformation + testing + lineage.
- **Airflow** — DAG-based workflow orchestration.
- **Tableau / PowerBI** — BI dashboards, drag-drop viz, data source connectors.

## Storytelling — `Storytelling/`
How to present data so people act on it.

### Core principles
1. **Start with the decision.** Every chart should change a choice. If no decision depends on it, cut it.
2. **Audience first.** Exec wants headline + implication. Peer DS wants method + caveats. Engineer wants repro + code.
3. **One chart, one idea.** If a slide has 3 messages, split it.
4. **Honesty beats polish.** Show confidence intervals. Flag biases. Note sample size.

### Structure (`Narrative/`)
- **Situation** — what is the current state? (baseline, trend, anomaly)
- **Complication** — what changed? what is the problem?
- **Question** — what do we need to decide?
- **Answer** — what does the data say? what is recommendation?

### Chart Choice (`ChartChoice/`)
| Goal | Use |
|------|-----|
| Compare values | bar |
| Trend over time | line |
| Part-of-whole | stacked bar (rarely pie) |
| Distribution | histogram, box, violin |
| Correlation | scatter |
| Geographic | choropleth |
| Flow / proportion transitions | sankey |
| Hierarchies | treemap |

### Color (`Color/`)
- Categorical = distinct hues. Keep under 7.
- Sequential (low→high) = single-hue gradient.
- Diverging (negative←0→positive) = 2-hue gradient through neutral.
- Colorblind-safe palettes (viridis, cividis).
- Red/green together → bad (colorblind + cultural).

### Annotations (`Annotations/`)
- Label the takeaway on the chart itself. Don't make reader decode.
- Highlight the one line/bar that matters.
- Add context: reference lines, event markers, goal lines.

### Dashboards (`Dashboards/`)
- Top-left = most important KPI.
- Layout = Z-pattern reading.
- Filters affect everything below; cascade top → bottom.
- Include "as-of" timestamp. Include data source link.

### Executive Presentation (`ExecutivePresentation/`)
- BLUF (Bottom Line Up Front): recommendation in first 30 seconds.
- 3 supporting points max.
- Appendix for details/methodology.
- No jargon in the main deck.

### Ethics (`Ethics/`)
- Don't cherry-pick time windows to flatter a trend.
- Don't truncate y-axis to exaggerate a change.
- Declare when sample is too small.
- Show who is excluded from the analysis.
- Honest > persuasive.

---

## Full project template
```
1. frame problem → write hypothesis doc (1 page)
2. pull data → profile it → document assumptions
3. EDA notebook → share for feedback early
4. baseline model → beat it before going complex
5. iterate: feature / model / eval
6. story draft → share with stakeholder
7. production plan: monitoring, retraining, rollback
```

## Classics
- "Storytelling with Data" — Cole Nussbaumer Knaflic
- "The Visual Display of Quantitative Information" — Edward Tufte
- "Trustworthy Online Controlled Experiments" — Kohavi et al.
- "Causal Inference: The Mixtape" — Scott Cunningham
