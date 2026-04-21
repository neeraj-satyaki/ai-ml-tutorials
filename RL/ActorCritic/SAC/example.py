"""SAC: max-entropy actor-critic. Stochastic continuous policy. Twin Q + entropy bonus.

J(pi) = E[ sum_t r_t + alpha * H(pi(.|s_t)) ]
"""
pseudocode = r"""
nets: pi (stochastic, Gaussian), Q1, Q2, Q1_target, Q2_target, learnable alpha
for step:
    a = pi(s)  # reparameterized sample
    store (s,a,r,s',d) in replay
    sample batch:
        with no grad:
            a', logp' = pi(s')
            q_t = min(Q1_t(s',a'), Q2_t(s',a')) - alpha * logp'
            y = r + gamma * (1-d) * q_t
        loss_Q = MSE(Q1(s,a), y) + MSE(Q2(s,a), y)
        a_new, logp = pi(s)
        loss_pi = E[ alpha*logp - min(Q1(s,a_new), Q2(s,a_new)) ]
        loss_alpha = -alpha * (logp + target_entropy).detach()
    soft-update targets
"""
print(pseudocode)
