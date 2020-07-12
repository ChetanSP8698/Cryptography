'''
*** A program for the cryptanalysis of Caesar cipher and identify the plaintext ***
'''

#All albhabet Frequencies in Known and meaningful English words
al_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 
			0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 
			0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

chi_square = [0] * 25


#Decryption of ciphertext with relative decryption key
def decrypt(ciphertext, s):
    pltext = ""
    for i in range(len(ciphertext)): 
        char = ciphertext[i]
  
        if (char.isupper()):
            pltext += chr((ord(char) - s - 65) % 26 + 65) 

        else: 
            pltext += chr((ord(char) - s - 97) % 26 + 97) 
  
    return pltext


#Finding the key by applying Chi - Square method
def find_key(ciphertext, k):
	l = len(ciphertext)
	cipher_freq = [0] * 26
	ci = [0] * 26
	ei = [0] * 26

	#ci and ei are Current value of letter and Expected value of letter.

	for i in range(65, 91):
		j = i-65
		cipher_freq[j] = ciphertext.count(chr(i))
		ci[j] = cipher_freq[j]
		ei[j] = al_freq[j] * l

	#Calculating Chi - Square value for every plain text with relative decryption key
	div = 0
	for m in range(0, l):
		num = (ci[int(ord(ciphertext[m]) - 65) % 26] - ei[int(ord(ciphertext[m]) - 65) % 26]) ** 2
		den = ei[int(ord(ciphertext[m]) - 65) % 26]
		div = num / den
		chi_square[k-1] += div

	for n in range(0, 26):
		if ci[n] == 0:
			chi_square[k-1] += ei[n]




#cipher = "aoljhlzhyjpwolypzvulvmaollhysplzaruvduhukzptwslzajpwolyzpapzhafwlvmzbizapabapvujpwolypudopjolhjoslaalypuaolwshpualeapzzopmalkhjlyahpuubtilyvmwshjlzkvduaolhswohila"
#cipher = "YMJHFJXFWHNUMJWNXTSJTKYMJJFWQNJXYPSTBSFSIXNRUQJXYHNUMJWX"

print("\nEnter the cipher text : ", end="")
cipher = str(input())

#Calculating 25 Decrypted(Plain) text with key value 1 to 25
for k in range(1, 26):
	ciphertext = decrypt(cipher, k)
	#print(ciphertext + str(k))
	ciphertext = ciphertext.upper()
	find_key(ciphertext, k)

#Getting the index of minimum chi - square value which is our Decryption key.
index = min(range(25), key = chi_square.__getitem__)
index += 1
index = int(index)
print("\nFound Decryption Key : " + str(index))
print("\nThe Decrypted Text (Plain Text) : ", end="")
print(decrypt(cipher, index))
print("\n")



