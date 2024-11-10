from queue import Queue

class Node:
    def __init__(self, level, profit, weight, bound=0):
        self.level = level        # Level of the node (index of item considered)
        self.profit = profit      # Current profit
        self.weight = weight      # Current weight
        self.bound = bound        # Upper bound on the maximum profit

def bound(node, W, weights, values, n):
    if node.weight >= W:
        return 0  # Bound is 0 if weight exceeds capacity
    
    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight

    while j < n and total_weight + weights[j] <= W:
        total_weight += weights[j]
        profit_bound += values[j]
        j += 1

    if j < n:
        profit_bound += (W - total_weight) * (values[j] / weights[j])
    
    return profit_bound

def knapsack_branch_and_bound(weights, values, W):
    n = len(values)
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    values, weights = zip(*items)
    
    Q = Queue()
    max_profit = 0

    root = Node(-1, 0, 0)
    root.bound = bound(root, W, weights, values, n)
    Q.put(root)

    while not Q.empty():
        current = Q.get()

        if current.level == n - 1:
            continue

        next_level = current.level + 1

        # Option 1: Include the item at next_level
        with_item = Node(next_level,
                         current.profit + values[next_level],
                         current.weight + weights[next_level])
        if with_item.weight <= W and with_item.profit > max_profit:
            max_profit = with_item.profit
        with_item.bound = bound(with_item, W, weights, values, n)
        if with_item.bound > max_profit:
            Q.put(with_item)

        # Option 2: Exclude the item at next_level
        without_item = Node(next_level, current.profit, current.weight)
        without_item.bound = bound(without_item, W, weights, values, n)
        if without_item.bound > max_profit:
            Q.put(without_item)

    return max_profit

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
print("Maximum profit in Knapsack =", knapsack_branch_and_bound(weights, values, W))
