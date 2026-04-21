"""Dyna-Q: Q-learning + learned model. After real step, do n simulated updates from model."""
import numpy as np

n_states, n_actions = 6, 2
Q = np.zeros((n_states, n_actions))
model = {}                              # (s,a) -> (r, s')
alpha, gamma, eps, n_plan = 0.1, 0.9, 0.1, 10
rng = np.random.default_rng(0)

def step(s, a):
    ns = max(0, s - 1) if a == 0 else min(n_states - 1, s + 1)
    r = 1.0 if ns == n_states - 1 else 0.0
    return ns, r, ns == n_states - 1

for ep in range(200):
    s = 0
    while True:
        a = rng.integers(n_actions) if rng.random() < eps else int(np.argmax(Q[s]))
        ns, r, done = step(s, a)
        Q[s, a] += alpha * (r + gamma * Q[ns].max() - Q[s, a])
        model[(s, a)] = (r, ns)
        # planning: n extra updates from cached model
        for _ in range(n_plan):
            (sp, ap), (rp, np_) = list(model.items())[rng.integers(len(model))]
            Q[sp, ap] += alpha * (rp + gamma * Q[np_].max() - Q[sp, ap])
        s = ns
        if done: break

print("Dyna-Q learned Q:\n", Q.round(2))
