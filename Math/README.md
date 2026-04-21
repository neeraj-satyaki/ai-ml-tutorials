# Math for ML / DL / RL

Math chapters needed. Each maps to folder in this tree.

## Linear Algebra — `LinearAlgebra/`
Backbone of ML. Everything is a tensor.
- **Vectors** — dot product, norms, projection, orthogonality.
- **Matrices** — mul, inverse, rank, trace, determinant, block matrices.
- **Eigen** — eigenvalues, eigenvectors, diagonalization, PCA foundation.
- **SVD** — A = U Σ V^T. Best low-rank approx, pseudoinverse, LoRA basis.
- **MatrixCalculus** — grads w.r.t. matrices: dL/dW, Kronecker product, vec trick.

## Calculus — `Calculus/`
Gradients drive every learning algorithm.
- **Limits** — continuity, ε-δ intuition.
- **Derivatives** — single-var, rules.
- **PartialDerivatives** — ∂f/∂x_i for multivariate loss.
- **Gradients** — ∇f direction of steepest ascent.
- **Chain** — backprop is repeated chain rule.
- **Integrals** — expectations, marginals, normalizing constants.
- **Taylor** — local approximations, 2nd-order methods.
- **Jacobian_Hessian** — vector-valued derivatives; curvature.

## Probability — `Probability/`
Models are probabilistic. Data is noisy.
- **BasicProb** — axioms, conditional prob, independence.
- **RandomVars** — discrete vs continuous, CDF, PDF, PMF.
- **Distributions** — Bernoulli, Binomial, Gaussian, Exponential, Poisson, Dirichlet, Categorical, Laplace.
- **Bayes** — P(θ|D) ∝ P(D|θ) P(θ). Priors, posteriors.
- **ExpectationVariance** — E[X], Var[X], covariance, correlation.
- **JointMarginal** — joint p(x,y), marginalization, conditioning.
- **MarkovChains** — P(s_t|s_{t-1}); foundation of RL + HMMs.

## Statistics — `Statistics/`
- **Descriptive** — mean, median, mode, variance, skew, kurtosis, quantiles.
- **Inference** — MLE, MAP, Bayesian estimation, sufficient statistics.
- **HypothesisTesting** — null/alt, p-values, t-test, chi-sq, ANOVA, multiple testing.
- **Confidence** — confidence intervals, bootstrap intervals.
- **Regression** — OLS, GLM, regularization (ridge, lasso).
- **Resampling** — bootstrap, jackknife, cross-validation.
- **Bayesian** — conjugate priors, MCMC (Gibbs, Metropolis-Hastings), Variational Inference.

## Optimization — `Optimization/`
Training = solving optimization problems.
- **GradientDescent** — SGD, momentum, Nesterov, Adam, AdamW, Lion, Sophia.
- **ConvexOpt** — convex functions/sets, duality, KKT.
- **Lagrangian** — constrained optimization, dual problem.
- **Convergence** — rates (linear, sublinear), Lipschitz, smoothness.
- **SecondOrder** — Newton, quasi-Newton (BFGS), natural gradient, K-FAC.
- **StochasticOpt** — minibatch SGD theory, variance reduction (SVRG).

## Information Theory — `InformationTheory/`
- **Entropy** — H(X) = -Σ p log p; uncertainty measure.
- **KL** — KL(p||q); VAE, RL policy constraints, distillation.
- **CrossEntropy** — CE(p,q); standard classification loss.
- **MutualInfo** — I(X;Y) = H(X) - H(X|Y); representation learning (InfoNCE).
- **Coding** — Shannon limit, lossless vs lossy compression.

## Discrete Math — `Discrete/`
- **SetLogic** — sets, boolean logic, predicate logic.
- **Combinatorics** — permutations, combinations, counting.
- **Graphs** — directed, weighted, bipartite; GNNs use these.
- **Trees** — BST, heaps, decision trees, tries.
- **Recurrences** — master theorem; dynamic programming.

## Numerical Methods — `NumericalMethods/`
Important for stable training.
- **FloatingPoint** — IEEE 754, fp16/bf16/fp8, precision loss.
- **NumericalStability** — log-sum-exp trick, catastrophic cancellation.
- **MatrixFactorization** — LU, QR, Cholesky.
- **Iterative** — Jacobi, conjugate gradient, Krylov.
- **Sampling** — inverse CDF, rejection, importance, MCMC.

## Geometry — `Geometry/`
- **EuclideanDistance** — L2, cosine similarity.
- **Manifolds** — locally Euclidean; basis of manifold learning (t-SNE, UMAP).
- **TopologyBasics** — open/closed, continuity, compactness.
- **RiemannianBasics** — metric tensor, natural gradient.

---

## Learning order (suggested)
1. Linear Algebra → Calculus → Probability (classical trio)
2. Statistics + Optimization (for classical ML)
3. Information Theory (for deep learning losses)
4. Numerical Methods (for stable training)
5. Discrete + Geometry (for GNNs, manifold learning, theory)

## Resources
- 3Blue1Brown — visual intuition (linalg, calc)
- MIT 18.06 (Strang) — Linear Algebra
- Boyd — Convex Optimization (free PDF)
- Deisenroth et al. — Mathematics for Machine Learning (free PDF)
- MacKay — Information Theory, Inference, Learning
