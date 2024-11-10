class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        # Value-to-weight ratio for greedy selection
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    # Sort items based on the value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0  # To store the total value of the knapsack
    for item in items:
        if capacity <= 0:
            break
        
        # If the item can be completely added to the knapsack
        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        else:
            # Take the fraction of the item that fits in the remaining capacity
            total_value += item.value * (capacity / item.weight)
            capacity = 0  # Knapsack is full now
    
    return total_value

# Example usage
if __name__ == "__main__":
    # Example items with value and weight
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    capacity = 50  # Capacity of the knapsack

    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in knapsack: {max_value}")
