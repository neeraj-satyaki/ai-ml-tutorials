"""Isolation Forest: anomaly detection via random-split tree depth."""
import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(0)
X_normal = rng.normal(0, 1, size=(200, 2))
X_outliers = rng.uniform(-6, 6, size=(20, 2))
X = np.vstack([X_normal, X_outliers])

iso = IsolationForest(contamination=0.1, random_state=0).fit(X)
pred = iso.predict(X)  # -1 = anomaly
print(f"flagged anomalies: {(pred == -1).sum()} (injected 20)")
