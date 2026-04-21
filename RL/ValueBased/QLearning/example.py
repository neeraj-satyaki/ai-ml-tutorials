"""Q-Learning: off-policy TD control. Q(s,a) += α[r + γ max_a' Q(s',a') - Q(s,a)]."""
import numpy as np

# 1D corridor: states 0..5, goal = 5
n_states, n_actions = 6, 2            # 0=left, 1=right
Q = np.zeros((n_states, n_actions))
alpha, gamma, eps = 0.1, 0.9, 0.1
rng = np.random.default_rng(0)

def step(s, a):
    ns = max(0, s - 1) if a == 0 else min(n_states - 1, s + 1)
    r = 1.0 if ns == n_states - 1 else 0.0
    done = ns == n_states - 1
    return ns, r, done

for ep in range(500):
    s = 0
    while True:
        a = rng.integers(n_actions) if rng.random() < eps else int(np.argmax(Q[s]))
        ns, r, done = step(s, a)
        Q[s, a] += alpha * (r + gamma * Q[ns].max() - Q[s, a])
        s = ns
        if done: break

print("learned Q:\n", Q.round(2))
