prices = {
	'ACME': 45.23,
	'AAPL': 612.78,
	'IBM': 205.55,
	'HPQ': 37.20,
	'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(f'min: {min_price}')

max_price = max(zip(prices.values(), prices.keys()))
print(f'max: {max_price}')

sorted_price = sorted(zip(prices.values(), prices.keys()))
print(f'sorted: {sorted_price}')