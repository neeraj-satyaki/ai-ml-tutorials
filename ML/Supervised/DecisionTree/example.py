"""Decision Tree: greedy splits maximizing info gain / gini."""
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = DecisionTreeClassifier(max_depth=3, random_state=0).fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
print(export_text(clf, feature_names=[f"f{i}" for i in range(4)]))
