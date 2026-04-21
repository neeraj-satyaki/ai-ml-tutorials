"""Label Propagation: spread labels through graph of sample similarity."""
import numpy as np
from sklearn.datasets import load_iris
from sklearn.semi_supervised import LabelPropagation

X, y = load_iris(return_X_y=True)
rng = np.random.default_rng(0)
y_partial = y.copy()
mask = rng.random(len(y)) < 0.7          # hide 70% labels
y_partial[mask] = -1

lp = LabelPropagation().fit(X, y_partial)
print(f"accuracy on hidden: {(lp.transduction_[mask] == y[mask]).mean():.3f}")
