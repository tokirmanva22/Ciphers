def encrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher += char
    elif  char.isupper():
      cipher += chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher += chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher
def decrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if not char.isalpha():
      cipher += char
    elif  char.isupper():
      cipher += chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher += chr((ord(char) - shift - 97) % 26 + 97)
  
  return cipher
 
text = open('cci.txt','r').read().strip('\n')
k = int(input("Enter shift Key: "))
print("original string: ", text)
x = int(input("press 1 for encryption or any key for decryption"))
if x==1:
	et = encrypt(text, k)
	print("after encryption: ", et)
	f1 = open('ccoe.txt','w+')
	f1.write(et)
	f1.close()
else:
	et = encrypt(text, k)
	dt = decrypt(et,k)
	f2 = open('ccod.txt','w+')
	print("encrypted text: ", et)
	print("after decryption: ",dt)
	f2.write(dt)
	f2.close()


