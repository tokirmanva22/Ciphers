def encrypt(t,k):
	kt = k
	n = len(t)
	if len(k) < n:
		for i in range(len(t) - len(k)):
			kt += (k[i % len(k)])
	ct = ''
	for i in range(n):
		if t[i] == ' ':
			x = ' '
			ct += x
		else:
			x = (ord(t[i]) + ord(kt[i])) % 26
			x += ord('A')
			ct += chr(x)
    
	return ct
def decrypt(t,k):
	kt = k
	n = len(t)
	c =0
	g = True
	for i in range(len(t) - len(k)):
		kt += (k[i % len(k)])
	ct = ''
	for i in range(n):
		if t[i] == ' ':
			x = ' '
			ct += x
		else:
			x = (ord(t[i]) - ord(kt[i])) % 26
			x += ord('A')
			ct += chr(x)
    
	return ct

def vigenere(x):
	if x==1:
		et = encrypt(text, k)
		print("after encryption: ", et)
		f1 = open('vcoe.txt','w+')
		f1.write(et)
		f1.close()
	else:
		et = encrypt(text, k)
		dt = decrypt(et,k)
		f2 = open('vcod.txt','w+')
		print("encrypted text: ", et)
		print("after decryption: ",dt)
		f2.write(dt)
		f2.close()

text = open('vcit.txt','r').read().strip('\n')
k = open('vcik.txt','r').read().strip('\n')
k = k.upper()
text = text.upper()
print("original string: ", text)
x = int(input("press 1 for encryption or any key for decryption"))
vigenere(x)