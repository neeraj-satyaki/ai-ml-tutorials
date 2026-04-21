"""Stacking: meta-learner trained on out-of-fold predictions of base models."""
from sklearn.datasets import load_iris
from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = StackingClassifier(
    estimators=[("rf", RandomForestClassifier(random_state=0)),
                ("svm", SVC(probability=True, random_state=0))],
    final_estimator=LogisticRegression(max_iter=500),
).fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
