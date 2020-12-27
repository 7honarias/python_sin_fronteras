def calcula_vol(r):
	vol = ((4/3) * 3.1416 * (r**3)) + 2
	return(vol)

radio = 6
result = calcula_vol(radio)
print(result)