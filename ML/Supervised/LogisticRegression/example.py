"""Logistic Regression: linear classifier with sigmoid output."""
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = LogisticRegression(max_iter=500).fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
