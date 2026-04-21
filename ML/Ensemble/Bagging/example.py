"""Bagging: train base learners on bootstrap samples, average predictions."""
from sklearn.datasets import load_iris
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = BaggingClassifier(DecisionTreeClassifier(), n_estimators=20,
                        random_state=0).fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
