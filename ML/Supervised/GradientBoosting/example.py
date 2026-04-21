"""Gradient Boosting: sequential trees each fitting residuals of prior."""
from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1,
                                 max_depth=3, random_state=0).fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
