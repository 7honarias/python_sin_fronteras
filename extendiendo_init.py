class Animal:
	def __init__(self, nombre, onomatopeya):
		self.nombre = nombre
		self.onomatopeya = onomatopeya
	def saludo(self):
		print("Hola, soy un ", self.tipo, "y mi sonido es el", self.onomatopeya)


class Gato(Animal):
	tipo = 'gato'
	def __init__(self, nombre, onomatopeya):
		Animal.__init__(self, nombre, onomatopeya)
		print('Hola soy una extencion')


class Perro(Animal):
	tipo = 'perro'
	def __init__(self, nombre, onomatopeya):
		super().__init__(nombre, onomatopeya)
		print('instanciando un perro')

class Canario(Animal):
	tipo = "canario"

perro = Perro("Jack", "ladrido")
perro.saludo()

gato = Gato("Kiara", "maullido")
gato.saludo()

canario = Canario("niño", "silvido")
canario.saludo()