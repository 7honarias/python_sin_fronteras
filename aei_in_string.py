voc = ['a', 'e', 'i', 'o', 'u']
frac = "hOla mundo!"
count = 0

for x in frac:
	y = x.lower()
	if y in voc:
		count += 1
print(count)