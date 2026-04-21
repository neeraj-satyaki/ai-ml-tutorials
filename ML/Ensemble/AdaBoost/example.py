"""AdaBoost: reweight misclassified samples; weak learners vote."""
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = AdaBoostClassifier(n_estimators=50, random_state=0).fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
