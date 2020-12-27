c = open("chanchitoFeliz.txt", "r+")  # a = append r = read w = write
print(c.readline())

for x in c:
	print(x)

c.write("\nAgrega un texto")

c.close()

# eliminar archivos
import os

if input():
	if os.path.exists('chachito.txt'):
		os.remove(chanchito.txt)
	else:
		print(archivo no existe)

os.rmdir('mi_carpeta') # elimina carpeta en el sistema