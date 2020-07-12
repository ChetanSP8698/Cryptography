#cipher_text = str(input())
cipher_text = "emtealemtalhtkeeepnax"

l = len(cipher_text)

col = 3
row = int(l / col)

a = []
q = 0
for i in range(0, row):
	a.append([])
	q = i
	for j in range(0, col):
		a[i].append(cipher_text[q])
		q = q + row

#print(a)

f = open("Output_file.txt", "a")
for z in range(0, 3):

	for x in range(0,row):
		f.write("\n")
		for y in range(0, col):
			y = (y + z) % 3
			f.write(a[x][y] + " ")
	
	f.write("\nPlain text could be :- ")

	for x in range(0,row):
		for y in range(0, col):
			y = (y + z) % 3
			f.write(a[x][y] + " ")
	
	f.write("\n")

for z in range(0, 3):

	for x in range(0,row):
		f.write("\n")
		for y in range(col-1, -1, -1):
			y = (y + z) % 3
			f.write(a[x][y] + " ")
	
	f.write("\nPlain text could be :- ")
	
	for x in range(0,row):
		for y in range(col-1, -1, -1):
			y = (y + z) % 3
			f.write(a[x][y] + " ")
	
	f.write("\n")


f.close()
