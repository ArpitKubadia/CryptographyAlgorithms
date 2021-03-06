from Crypto.Cipher import Blowfish
from datetime import datetime
from Crypto import Random
from struct import pack
# Encryption
from xlwt import Workbook

wb=Workbook()
output=wb.add_sheet('Blowfish')
output.write(0,0,'Message Size')
output.write(0,1,'Encryption time')
output.write(0,2,'Decryption time')
output.write(0,3,'Cipher text Size')


#print(message)
#time1=time.time()
def encryption(message):
	start=datetime.now()
	cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
	plen = bs - divmod(len(message),bs)[1]
	padding = [plen]*plen
	padding = pack('b'*plen, *padding)
	cipher_text=iv + cipher.encrypt(message + padding)
	end=datetime.now()
	total=end-start
	total=total.total_seconds()
	print("Encryption time:",total)
	return cipher_text,total


#print (cipher_text)
#time2=time.time()
#print((time2-time1)*1000)

def decryption(ciphertext):
	start=datetime.now()
	iv = ciphertext[:bs]
	ciphertext = ciphertext[bs:]
	cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
	msg = cipher.decrypt(ciphertext)

	last_byte = msg[-1]
	msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
	plain_text=msg
	end=datetime.now()
	total=end-start
	total=total.total_seconds()
	print("Decryption time:",total)
	return plain_text,total


bs = Blowfish.block_size
print("Block Size",bs)
key=b"Jsp3nd762MAO283N"
iv = Random.new().read(bs)


#message=b'A really secret message. Not for prying eyes.'
for i in range (8):
	f=open('ciphertext_1mb.txt',encoding="ANSI")
	inp=f.read()
	#message="Hello please try to encrypt this using Blowfish"
	message='null'
	for j in range(2**i):
		message+=inp
	output.write(i+1,0,round(len(message)/(1024*1024)))
	print("Message size(mb): ", len(message)/(1024*1024))
	message=str.encode(message)
	cipher_text,time_enc=encryption(message)
	plain_text,time_dec=decryption(cipher_text)
	#print(message)
	#print(plain_text)	
	print(message==plain_text)
	#print("Message size(mb): ", len(message)/(1024*1024))
	print("Cipher text size(mb): ",len(cipher_text)/(1024*1024))
	print("\n\n")

	output.write(i+1,1,time_enc)
	output.write(i+1,2,time_dec)
	output.write(i+1,3,len(cipher_text)/(1024*1024))

wb.save('Blowfish.xls')

#print(plain_text)

#print(timeit.timeit(encryption))