from Crypto.Cipher import DES3
from datetime import datetime
from Crypto import Random
# Encryption


#print(message)
#time1=time.time()
def encryption(message):
	start=datetime.now()
	cipher = DES3.new(key, DES3.MODE_OFB, iv)
	cipher_text=cipher.encrypt(message)
	end=datetime.now()
	total=end-start
	total=total.total_seconds()
	print("Encryption time:",total)
	return cipher_text


#print (cipher_text)
#time2=time.time()
#print((time2-time1)*1000)

def decryption(cipher_text):
	start=datetime.now()
	cipher = DES3.new(key, DES3.MODE_OFB, iv)
	plain_text=cipher.decrypt(cipher_text)
	end=datetime.now()
	total=end-start
	total=total.total_seconds()
	print("Decryption time:",total)
	return plain_text

key=b"Jsp3nd762MAO283N"
#iv=b"This is an IV456"
iv=Random.new().read(DES3.block_size)
print("Block Size: ",DES3.block_size)

#message=b'A really secret message. Not for prying eyes.'
for i in range (8):
	f=open('ciphertext_1mb.txt',encoding="ANSI")
	inp=f.read()
	message='null'
	for j in range(2**i):
		message+=inp
	print("Message size(mb): ", len(message)/(1024*1024))
	message=str.encode(message)
	cipher_text=encryption(message)
	plain_text=decryption(cipher_text)	
	#print(message)
	#print(plain_text)
	print(message==plain_text)
	#print("Message size(mb): ", len(message)/(1024*1024))
	print("Cipher text size(mb): ",len(cipher_text)/(1024*1024))
	print("\n\n")



#print(plain_text)

#print(timeit.timeit(encryption))