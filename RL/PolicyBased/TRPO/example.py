"""TRPO: trust-region policy opt via KL constraint + conjugate-gradient.

Complex: needs Fisher-vector products + line search. Pseudocode below.
PPO is practical simplification of this method.
"""

pseudocode = r"""
for iteration:
    rollout trajectories tau ~ pi_theta_old
    compute advantages A_t (GAE)
    compute policy gradient g = E[ grad log pi(a|s) * A ]
    compute Fisher-vec product: F*x = E[ grad log pi * (grad log pi)^T * x ]
    solve F * step = g via conjugate gradient
    scale step so KL(pi_old || pi_new) <= delta
    backtracking line search: accept largest step improving surrogate
    update theta
"""
print(pseudocode)
