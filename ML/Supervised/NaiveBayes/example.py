"""Naive Bayes: P(y|x) via Bayes + feature independence assumption."""
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = GaussianNB().fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
