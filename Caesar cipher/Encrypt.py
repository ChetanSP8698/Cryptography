def encrypt(ciphertext, s): 
    pltext = ""
    for i in range(len(ciphertext)): 
        char = ciphertext[i]
  
        if (char.isupper()):
            pltext += chr((ord(char) + s-65) % 26 + 65) 

        else: 
            pltext += chr((ord(char) + s - 97) % 26 + 97) 
  
    return pltext
  

print("Enter Plain text : ", end="")
plaintext = str(input())
#ciphertext = "MEETMEATELEPHANTSLAKEATNOON"
print("Key : ", end="")
s = int(input())
print("Plain text  : " + plaintext)
print("Shift : " + str(s))
print("Cipher text: " + encrypt(plaintext,s))