
def C_R_T(b, n):
    sum = 0
    N = 1
    for items in n:
    	N *= items
    for y, x in zip(b, n):
        p = N // x
        sum += y * p * Mul_Inv(p, x)
    return sum % N

def Mul_Inv(i, j):
	i = i % j; 
	for x in range(1, j) : 
		if ((i * x) % j == 1) :
			return x 
	return 1
 
def gcd(a, b):
    if a == b:
        return a 
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

if __name__ == '__main__':
	eq = int(input("Enter the number of congruence : "))

	n = []
	b = []
	flag = 1

	for i in range(0, eq):
		b.append(int(input("p = ")))
		n.append(int(input("     mod ")))
	
	for i in range(0, len(b) - 1):
		for j in range (i + 1, len(b)):
			if gcd(n[i], n[j]) != 1:
				print(str(n[i]) + " and " + str(n[j]) + " are not co-prime")
				flag = 0
				exit()
	if flag == 1:
		print("p = ", end='')
		print(C_R_T(b, n))
