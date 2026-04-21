"""A3C: asynchronous A2C. Multiple workers update shared net asynchronously.

Pseudocode outline below.
"""
pseudocode = r"""
shared_net = ActorCritic()
for each worker in parallel:
    local_net = copy(shared_net)
    while True:
        rollout t steps with local_net
        compute grads of A2C loss on local_net
        asynchronously apply grads to shared_net
        sync local_net <- shared_net
"""
print(pseudocode)
