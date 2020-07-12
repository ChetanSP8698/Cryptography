def decrypt(ciphertext, s): 
    pltext = ""
    for i in range(len(ciphertext)): 
        char = ciphertext[i]
  
        if (char.isupper()):
            pltext += chr((ord(char) - s-65) % 26 + 65) 

        else: 
            pltext += chr((ord(char) - s - 97) % 26 + 97) 
  
    return pltext
  

ciphertext = "EXXEGOEXSRGI"
s = 4
print("Cipher  : " + ciphertext)
print("Shift : " + str(s))
print("Plain text: " + decrypt(ciphertext,s))