"""SARSA: on-policy TD. Uses actually-taken next action a', not max."""
import numpy as np

n_states, n_actions = 6, 2
Q = np.zeros((n_states, n_actions))
alpha, gamma, eps = 0.1, 0.9, 0.1
rng = np.random.default_rng(0)

def step(s, a):
    ns = max(0, s - 1) if a == 0 else min(n_states - 1, s + 1)
    r = 1.0 if ns == n_states - 1 else 0.0
    return ns, r, ns == n_states - 1

def pick(s):
    return rng.integers(n_actions) if rng.random() < eps else int(np.argmax(Q[s]))

for ep in range(500):
    s = 0
    a = pick(s)
    while True:
        ns, r, done = step(s, a)
        na = pick(ns)
        Q[s, a] += alpha * (r + gamma * Q[ns, na] - Q[s, a])
        s, a = ns, na
        if done: break

print("learned Q:\n", Q.round(2))
