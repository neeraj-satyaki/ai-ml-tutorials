"""SVM: maximize margin hyperplane. RBF kernel for non-linear."""
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
clf = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1.0)).fit(Xtr, ytr)
print(f"accuracy = {clf.score(Xte, yte):.3f}")
