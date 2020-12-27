#!/usr/bin/python3

name = "Pedro"
lastname = "Perez"

fullName = name + ' ' + lastname
b = len(fullName) - 1
while b >= 0:
	print(fullName[b], end='')
	b -= 1
print()

# tambien se puede dar vuelta al String de la siguiente manera
print(fullName[::-1])
