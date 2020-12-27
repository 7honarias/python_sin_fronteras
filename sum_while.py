#!/usr/bin/python3
result = 0

print("ingresa valores a sumar o basta para salir")
while(True):
	valor = input("ingresa valor: ")
	if valor == 'basta':
		break
	else:
		try:
			x = int(valor)
		except:
			print("valor invalido")
			exit()
	result += x
print(result)