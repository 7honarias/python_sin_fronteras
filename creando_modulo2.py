from camelcase import CamelCase
import creando_modulo as xs
# as usado para cambiar el nombre del modulo

print(xs.mascotas)
xs.saludo("Jhon")

c = CamelCase()
s = "esta oracion necesita camelcase"
camelcased = c.hump(s)
print(camelcased)


#pip3 list muestra los modulos intalados en la maquina
#pip3 unistall camelcase desinstala el modulo
