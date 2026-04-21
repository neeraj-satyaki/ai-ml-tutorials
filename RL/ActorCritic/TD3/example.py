"""TD3: DDPG + 3 fixes — twin critics (min of Q1,Q2), delayed actor updates, target-policy smoothing."""
pseudocode = r"""
for step:
    a = clip(actor(s) + noise, a_low, a_high)
    store transition
    sample batch
    with no grad:
        a' = clip(actor_t(s') + clip(noise, -c, c), a_low, a_high)  # smoothing
        y = r + gamma * (1-d) * min(Q1_t(s',a'), Q2_t(s',a'))
    loss_Q1 = MSE(Q1(s,a), y); loss_Q2 = MSE(Q2(s,a), y)
    update Q1, Q2
    every d steps:
        loss_pi = -Q1(s, actor(s)).mean()
        update actor
        soft-update all target nets
"""
print(pseudocode)
