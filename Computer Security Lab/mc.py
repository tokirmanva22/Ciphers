def encrypt(txt, dic):
	string = ''
	for i in range(len(txt)):
		string += dic[txt[i].lower()]
	return string

def decrypt(txt, dic):
	string = ''
	for i in range(len(txt)):
		string += dic[txt[i]]
	return string


s ='abcdefghijklmnopqrstuvwxyz'
dic = {}
dic1 = {}
dic[' '] = ' '
dic1[' '] = ' '
f = open('mcik.txt','r')
key = f.read().strip('\n')
f1 = open('mcit.txt','r')
text = f1.read().strip('\n')
if len(key) != 26:
	raise ValueError("Please Check Your key,Key Should be length 26 only")
flg=0
for i in key:
	if key.count(i) > 1:
		raise ValueError("repetation of characters are not allow")
		flg=1
		break
if flg==0:
	for i in range(26):
		dic[s[i]] = key[i].upper()
	for i in range(26):
		dic1[key[i].upper()] = s[i]

	x = int(input("press 1 for encryption or any key for decryption"))
	if x==1:
		et = encrypt(text, dic)
		print("after encryption: ", et)
		f2 = open('mcoe.txt','w+')
		f2.write(et)
		f2.close()
	else:
		et = encrypt(text, dic)
		dt = decrypt(et,dic1)
		f3 = open('mcod.txt','w+')
		print("encrypted text: ", et)
		print("after decryption: ",dt)
		f3.write(dt)
		f3.close()
f.close()
f1.close()



