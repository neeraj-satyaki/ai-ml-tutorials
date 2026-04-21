"""MCTS: tree search with 4 phases — Select (UCT), Expand, Simulate, Backpropagate."""
import math
import random

class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = {}   # action -> Node
        self.n = 0
        self.w = 0.0
    def uct(self, c=1.4):
        if self.n == 0: return float("inf")
        return self.w / self.n + c * math.sqrt(math.log(self.parent.n) / self.n)

def mcts(root_state, actions, rollout_fn, n_iter=500):
    root = Node()
    for _ in range(n_iter):
        node, state = root, list(root_state)
        # select
        while node.children and all(a in node.children for a in actions(state)):
            a, node = max(node.children.items(), key=lambda kv: kv[1].uct())
            state = transition(state, a)
        # expand
        legal = actions(state)
        if legal:
            a = random.choice([a for a in legal if a not in node.children])
            node.children[a] = Node(parent=node)
            node = node.children[a]
            state = transition(state, a)
        # simulate (rollout)
        reward = rollout_fn(state)
        # backprop
        while node is not None:
            node.n += 1
            node.w += reward
            node = node.parent
    return max(root.children.items(), key=lambda kv: kv[1].n)[0]

# toy env: pick a number, reward = 1 if picked 3
def transition(state, a): return state + [a]
def rollout(state): return 1.0 if 3 in state else 0.0
def legal(state): return [] if len(state) >= 1 else [0, 1, 2, 3, 4]

best = mcts([], legal, rollout, n_iter=200)
print("MCTS best first action:", best)
