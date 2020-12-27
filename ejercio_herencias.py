#!/usr/bin/python3

class Animal:
	def __init__(self, nombre, onomatopeya):
		self.nombre = nombre
		self.onomatopeya = onomatopeya
	def saludo(self):
		print("Hola, soy un ", self.tipo, "y mi sonido es el", self.onomatopeya)


class Gato(Animal):
	tipo = 'gato'


class Perro(Animal):
	tipo = 'perro'

class Canario(Animal):
	tipo = "canario"

perro = Perro("Jack", "ladrido")
perro.saludo()

gato = Gato("Kiara", "maullido")
gato.saludo()

canario = Canario("niño", "silvido")
canario.saludo()