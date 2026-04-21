"""Random Forest: bagged decision trees with feature subsampling."""
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = RandomForestClassifier(n_estimators=100, random_state=0).fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
print("feature importances:", clf.feature_importances_.round(3))
