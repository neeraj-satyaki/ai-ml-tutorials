"""XGBoost: regularized gradient boosting, 2nd-order Taylor, fast.

Install: pip install xgboost
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import xgboost as xgb

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = xgb.XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1,
                       eval_metric="mlogloss").fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
