
class Item:
	def __init__(self, profit, weight):
		self.profit = profit
		self.weight = weight

def fractionalKnapsack(W, arr):
	arr.sort(key=lambda x: (x.profit/x.weight), reverse=True) 
	finalvalue = 0.0
	for item in arr:
		if item.weight <= W:
			W -= item.weight
			finalvalue += item.profit
		else:
			finalvalue += item.profit * W / item.weight
			break
	return finalvalue

if __name__ == "__main__":
	W =int(input("Enter Capacity:"))
	arr =[]
	N=int(input("Enter no. of items:\n"))
	for i in range(0,N):
		profit=int(input("Enter profit of item:\n"))
		weight=int(input("Enter weight of item:\n"))
		obj=Item(profit,weight)
		arr.append(obj)
	
	max_val = fractionalKnapsack(W, arr)
	print(max_val)
