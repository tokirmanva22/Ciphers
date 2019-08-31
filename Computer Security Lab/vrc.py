def encrypt(text,key):
	ct = ""
	ptr = 0
	for char in text:
		ct = ct + chr(ord(char) ^ ord(key[ptr]))
		ptr = ptr + 1
		if ptr == len(key):
			ptr = 0
	return ct
def decrypt(text,key):
	ct = ""
	ptr = 0
	for char in text:
		ct = ct + chr(ord(char) ^ ord(key[ptr]))
		ptr = ptr + 1
		if ptr == len(key):
			ptr = 0
	return ct

def vigenere(x):
	if x==1:
		et = encrypt(text, k)
		print("after encryption: ", et)
		f1 = open('vrcoe.txt','w+')
		f1.write(et)
		f1.close()
	else:
		et = encrypt(text, k)
		dt = decrypt(et,k)
		f2 = open('vrcod.txt','w+')
		print("encrypted text: ", et)
		print("after decryption: ",dt)
		f2.write(dt)
		f2.close()

text = open('vrcit.txt','r').read().strip('\n')
k = open('vrcik.txt','r').read().strip('\n')
k = k.upper()
text = text.upper()
print("original string: ", text)
x = int(input("press 1 for encryption or any key for decryption in Vernam Ciepher"))
vigenere(x)
