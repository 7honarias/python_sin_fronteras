def mayor(usuario):
	return (usuario.edad >= 18)

class Usuario:
	def __init__(self, edad, nombre):
		self.edad = edad
		self.nombre = nombre

usuario = Usuario(18, "Chanchito")

print(mayor(usuario))