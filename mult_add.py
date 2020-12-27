def mult(a, b):
	result = 0
	for x in range(0, b):
		result += a
	return (result)

a, b = input().split()

a = int(a)
b = int(b)

m = mult(a, b)
print(m)