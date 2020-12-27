import os

e = open("names.txt", "a")
name, lastname = input("ingresa nombre y apellido ").split()
e.write("\nnombre: {}".format(name))
e.write("\napellido: {}".format(lastname))

e.close()