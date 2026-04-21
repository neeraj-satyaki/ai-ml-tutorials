# EDA Coefficients & Statistics

Reference of coefficients / statistics used in Exploratory Data Analysis.
Each entry: **formula/definition**, **when to use**, **example scenario**.

---

## 1. Central Tendency

### Mean (μ)
- **Formula:** μ = Σx_i / n.
- **When:** symmetric distributions; no heavy outliers.
- **Scenario:** average transaction value when distribution is near-Gaussian (e.g., daily latency of healthy API).

### Median
- **When:** skewed data or outliers present.
- **Scenario:** household income (rich tail distorts mean); response times with long-tail spikes.

### Mode
- **When:** categorical or multimodal numeric.
- **Scenario:** most common plan tier; dominant browser.

### Trimmed Mean (10%, 20%)
- **When:** mild outliers but want mean-like summary.
- **Scenario:** sports scoring, reviewer ratings.

### Geometric Mean
- **When:** multiplicative processes; rates; ratios.
- **Scenario:** avg portfolio growth rate across years; avg speed-up across benchmarks.

### Harmonic Mean
- **When:** averaging rates where denominators matter.
- **Scenario:** avg mph over fixed distance; F1-score combines precision + recall (harmonic mean).

---

## 2. Spread / Dispersion

### Variance (σ²) / Std Dev (σ)
- **When:** distribution roughly symmetric.
- **Scenario:** variability of temperature readings; measurement error.

### IQR (Q3 − Q1)
- **When:** skewed data; robust spread.
- **Scenario:** describing salary spread in a team; building boxplot whiskers.

### MAD (Median Absolute Deviation)
- **When:** very heavy-tailed or outlier-heavy data.
- **Scenario:** anomaly detection in sensor streams; robust scaling in ML features.

### Coefficient of Variation (CV = σ/μ)
- **When:** comparing spread across different-scale variables.
- **Scenario:** which metric varies more relative to its own scale — daily CPU (0-100) vs daily signups (0-10k).

---

## 3. Distribution Shape

### Skewness (γ₁)
- **When:** decide if log/sqrt transform needed; assess symmetry.
- **Scenario:** income data — right-skewed → log-transform before modeling.

### Kurtosis (excess = γ₂ − 3)
- **When:** assess tail heaviness; risk modeling.
- **Scenario:** financial returns show high kurtosis → fat tails → VaR underestimates risk if assume Gaussian.

### Jarque-Bera
- **When:** quick normality test combining skew + kurtosis.
- **Scenario:** checking regression residuals for normality assumption.

---

## 4. Association: Numeric × Numeric

### Pearson r
- **When:** linear, roughly bivariate normal, no extreme outliers.
- **Scenario:** height vs weight in adults; ad spend vs sales in a linear regime.
- **Avoid:** nonlinear U-shapes (returns near-zero even with strong dep).

### Spearman ρ
- **When:** monotonic but not linear; ordinal data; outliers present.
- **Scenario:** rank of SAT score vs rank of GPA; exposure dose vs severity score.

### Kendall τ
- **When:** small sample + ties; more robust than Spearman.
- **Scenario:** evaluating agreement between two raters' rankings; survey ordinal data.

### Distance Correlation (dCor)
- **When:** suspect nonlinear or non-functional dependence; want a coefficient that is 0 iff independent.
- **Scenario:** finding hidden relationships between input features and targets that Pearson misses (e.g., y = x²).

### Maximal Information Coefficient (MIC)
- **When:** large screening for any relationship type.
- **Scenario:** gene expression screens for pairwise associations.

### Mutual Information
- **When:** feature selection; any-type dependence.
- **Scenario:** picking top-k features for a classifier in sklearn pipeline.

### Coefficient of Determination (R²)
- **When:** regression model quality.
- **Scenario:** linear fit of demand vs price: R²=0.85 means 85% of variance explained.

---

## 5. Association: Categorical × Categorical

### Chi-square (χ²) test
- **When:** test independence of 2 categorical variables.
- **Scenario:** is "subscription tier" independent of "region"?

### Cramér's V
- **When:** you need a [0,1] effect-size (chi-square scales with n).
- **Scenario:** reporting strength of association across multiple 2-way tables in a dashboard.

### Phi (φ) — 2×2 only
- **When:** binary × binary.
- **Scenario:** clicked (y/n) vs is_mobile (y/n) on an ad.

### Contingency Coefficient / Tschuprow's T
- **When:** alternatives to Cramér's V; rarely used now.

---

## 6. Association: Categorical × Numeric

### Point-biserial r_pb
- **When:** binary group × continuous outcome.
- **Scenario:** gender (M/F encoded) vs test score.

### Eta squared (η²)
- **When:** one-way ANOVA effect size.
- **Scenario:** how much variance in latency is explained by server region (A/B/C/D)?

### Cohen's d
- **When:** standardized mean difference between two groups.
- **Scenario:** A/B test effect size — control vs treatment conversion mean. d=0.5 ≈ medium effect.

### Hedges' g
- **When:** small samples (Cohen's d is biased).
- **Scenario:** clinical trial with ~20 per arm.

### Glass's Δ
- **When:** treatment vs control with differing variances; use control SD.

---

## 7. Association: Ordinal

### Spearman ρ (see above)
- **Scenario:** Likert scale × Likert scale.

### Goodman-Kruskal γ
- **When:** ordinal-ordinal; tolerant of ties.
- **Scenario:** satisfaction level × purchase frequency (both ordinal).

### Somers' D
- **When:** asymmetric ordinal relationship (which predicts which).
- **Scenario:** credit rating predicting default bucket.

---

## 8. Time Series

### Autocorrelation (ACF)
- **When:** check if future ~ past; pick MA lag.
- **Scenario:** daily active users — find weekly seasonality (spike at lag 7).

### Partial Autocorrelation (PACF)
- **When:** pick AR lag.
- **Scenario:** ARIMA model identification.

### Ljung-Box Q
- **When:** post-fit — confirm residuals have no autocorrelation.
- **Scenario:** after ARIMA, verify residual whiteness.

### ADF / KPSS
- **When:** test stationarity before AR/ARIMA.
- **Scenario:** GDP time series — difference until ADF rejects unit root.

### Granger causality
- **When:** does X_{t-k} help predict Y_t beyond Y's own lags.
- **Scenario:** does ad spend Granger-cause sales in weekly data? (Not actual causation!)

---

## 9. Multicollinearity

### Pearson correlation matrix
- **When:** first pass.
- **Scenario:** find redundant pairs (|r|>0.9) for removal.

### VIF (Variance Inflation Factor)
- **When:** better than pairwise for 3+ feature redundancy.
- **Scenario:** in a linear model with 20 features, identify which have VIF>5 → drop or combine.

### Condition number of X^T X
- **When:** numerical stability check.
- **Scenario:** OLS diverging — κ>30 signals ill-conditioned.

---

## 10. Outlier Detection

### Z-score
- **When:** Gaussian-ish data.
- **Scenario:** sensor reading 5σ above mean — likely malfunction.

### Modified Z (MAD-based)
- **When:** non-Gaussian / heavy-tailed.
- **Scenario:** ad impressions (long tail) — use modified Z instead of mean/std.

### IQR rule (1.5×IQR)
- **When:** any distribution; quick.
- **Scenario:** boxplot outlier flagging for income.

### Grubbs / Dixon
- **When:** single outlier test in small sample (lab experiments).

### Cook's distance
- **When:** flag influential points in regression.
- **Scenario:** one big customer account distorting a linear pricing model.

### Leverage / DFFITS / DFBETAS
- **When:** regression diagnostics.

---

## 11. Distribution Fits

### Kolmogorov-Smirnov (KS)
- **When:** compare sample to theoretical dist, or two samples.
- **Scenario:** A/B test distributional shift — compare latency CDFs.

### Anderson-Darling
- **When:** more tail-sensitive normality test.
- **Scenario:** checking whether a credit-score follows normal distribution (important for tail behavior).

### Shapiro-Wilk
- **When:** small samples (n ≤ 2000); powerful normality.
- **Scenario:** validating residual normality in a small lab experiment.

### QQ-plot (visual, not coefficient)
- **Scenario:** visually confirm residual normality.

### Chi-square goodness-of-fit
- **When:** binned distribution vs expected.
- **Scenario:** dice roll fairness; survey response category expected frequencies.

---

## 12. Regression Diagnostics

### R² / Adjusted R²
- **When:** compare models (Adj penalizes extra features).
- **Scenario:** linear model predicting house price.

### AIC / BIC
- **When:** model selection penalizing complexity.
- **Scenario:** picking ARIMA order; feature selection.

### RMSE / MAE / MAPE / sMAPE
- **When:** prediction error reporting (MAPE for % errors; MAE robust).
- **Scenario:** MAPE for demand forecast business reports; RMSE for Kaggle regression.

### Durbin-Watson
- **When:** detect autocorrelated residuals.
- **Scenario:** time-series regression — DW near 2 = OK; <1.5 = positive AC.

### Breusch-Pagan / White test
- **When:** heteroskedasticity detection.
- **Scenario:** variance of residuals grows with x → use robust SEs / WLS.

---

## 13. Hypothesis Tests (common statistics)

### t-statistic
- **When:** compare two means; small sample.
- **Scenario:** A/B test on avg session time.

### z-statistic
- **When:** large sample or known variance.
- **Scenario:** conversion rate A/B test (proportions).

### F-statistic
- **When:** variance ratio; ANOVA; nested model comparison.
- **Scenario:** one-way ANOVA comparing ≥3 group means.

### Mann-Whitney U
- **When:** non-parametric 2-sample.
- **Scenario:** comparing engagement across 2 groups when distributions aren't normal.

### Wilcoxon signed-rank
- **When:** paired non-parametric.
- **Scenario:** before/after measurement on same users.

### Kruskal-Wallis
- **When:** non-parametric ≥3 groups.
- **Scenario:** comparing medians of 4 regions' median order value.

---

## 14. Effect Sizes

### Cohen's d (see §6)
- **Scenario:** A/B tests — report effect + p-value; avoids "statistically but not practically" significant.

### η² / ω²
- **When:** ANOVA.

### Odds ratio / Risk ratio
- **When:** 2×2 binary outcome × group.
- **Scenario:** medical exposure (smoker vs not) → lung cancer OR.

### Cliff's δ
- **When:** non-parametric effect size.
- **Scenario:** ordinal outcome between two groups.

---

## 15. Categorical Distribution Summaries

### Gini impurity
- **When:** decision tree splits.
- **Scenario:** CART measures impurity drop per split.

### Shannon entropy
- **When:** uncertainty; ID3/C4.5 info gain; also text compression.
- **Scenario:** measure class-imbalance severity.

### Herfindahl-Hirschman Index (HHI)
- **When:** market concentration.
- **Scenario:** supplier concentration — HHI>2500 = concentrated.

---

## 16. ML-flavored

### SHAP values
- **When:** per-prediction feature attribution.
- **Scenario:** explain why model denied a specific loan.

### Permutation importance
- **When:** model-agnostic global importance.
- **Scenario:** sanity-check feature importance vs tree's built-in.

### Partial Dependence / ICE
- **When:** marginal effect curves.
- **Scenario:** visualize price elasticity in a model.

---

## 17. Cheat Sheet — picking the right tool

| Goal | Pick |
|------|------|
| Symmetric central tendency | Mean |
| Skewed central tendency | Median |
| Linear num-num | Pearson r |
| Monotonic / robust num-num | Spearman ρ |
| Any dependence num-num | Distance corr / MI |
| Cat-Cat independence | χ² + Cramér's V |
| Cat-Num groups effect | Cohen's d / η² |
| Outliers Gaussian | Z-score |
| Outliers non-Gaussian | Modified Z / IQR |
| Multicollinearity | Pearson → VIF → cond κ |
| Shape | Skew + Kurtosis + QQ |
| Normality | Shapiro (small) / AD (general) |
| Time series memory | ACF / PACF |
| Stationarity | ADF + KPSS |
| Effect size (means) | Cohen's d / Hedges' g |
| Effect size (proportions) | Odds Ratio / Risk Ratio |

---

## End-to-end EDA recipe with these

```python
import pandas as pd, scipy.stats as st, numpy as np

# 1. Univariate
df.describe().T                       # mean, std, quartiles
df.skew(); df.kurt()                  # shape
df.isna().mean() * 100                # missing %

# 2. Bivariate numeric
df.corr(method="pearson")
df.corr(method="spearman")

# 3. Bivariate categorical (Cramér's V)
from scipy.stats import chi2_contingency
def cramers_v(x, y):
    c = pd.crosstab(x, y); chi2 = chi2_contingency(c)[0]
    n = c.values.sum(); r, k = c.shape
    return np.sqrt(chi2 / (n * (min(r, k) - 1)))

# 4. Categorical × numeric (Cohen's d)
def cohens_d(a, b):
    pooled = np.sqrt(((len(a)-1)*a.var()+(len(b)-1)*b.var())/(len(a)+len(b)-2))
    return (a.mean() - b.mean()) / pooled

# 5. Multicollinearity (VIF)
from statsmodels.stats.outliers_influence import variance_inflation_factor
vifs = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# 6. Outliers — modified Z
med = np.median(x); mad = np.median(np.abs(x - med))
mod_z = 0.6745 * (x - med) / mad
outliers = np.abs(mod_z) > 3.5

# 7. Normality — Shapiro
st.shapiro(x).pvalue > 0.05  # non-reject → treat as normal

# 8. Time series — ADF + ACF
from statsmodels.tsa.stattools import adfuller, acf
adfuller(series).pvalue                 # <0.05 → stationary
acf(series, nlags=40)                   # seasonality
```
