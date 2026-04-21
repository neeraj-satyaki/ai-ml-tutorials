"""GMM: soft clustering as mixture of gaussians fit by EM."""
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=3, random_state=0)
gmm = GaussianMixture(n_components=3, random_state=0).fit(X)
print("means:\n", gmm.means_.round(2))
print("weights:", gmm.weights_.round(3))
