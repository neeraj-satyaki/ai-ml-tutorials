"""Linear Regression: fit y = w*x + b by minimizing MSE."""
import numpy as np
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(0)
X = rng.uniform(0, 10, size=(100, 1))
y = 3 * X.squeeze() + 7 + rng.normal(0, 1, size=100)

model = LinearRegression().fit(X, y)
print(f"learned w={model.coef_[0]:.2f} b={model.intercept_:.2f}  (true 3, 7)")
print(f"R^2 = {model.score(X, y):.3f}")
