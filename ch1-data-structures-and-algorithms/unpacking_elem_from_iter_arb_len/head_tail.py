items = [1, 10, 7, 4, 5, 9]

head, *tail = items
print(head)
print(tail)

print()

def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else head

result = sum(items)
print(result)