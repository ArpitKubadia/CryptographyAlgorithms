from Crypto.Cipher import ARC2
from datetime import datetime
from Crypto import Random
# Encryption
from xlwt import Workbook

wb=Workbook()
output=wb.add_sheet('ARC2')
output.write(0,0,'Message Size')
output.write(0,1,'Encryption time')
output.write(0,2,'Decryption time')
output.write(0,3,'Cipher text Size')

#print(message)
#time1=time.time()
def encryption(message):
	start=datetime.now()
	cipher = ARC2.new(key, ARC2.MODE_CFB, iv)
	cipher_text = cipher.encrypt(message)
	end=datetime.now()
	total=end-start
	total=total.total_seconds()
	print("Encryption time:",total)
	return cipher_text,total


#print (cipher_text)
#time2=time.time()
#print((time2-time1)*1000)

def decryption(cipher_text):
	start=datetime.now()
	cipher = ARC2.new(key, ARC2.MODE_CFB, iv)	
	plain_text = cipher.decrypt(cipher_text)
	end=datetime.now()
	total=end-start
	total=total.total_seconds()
	print("Decryption time:",total)
	return plain_text,total

key=b"Jsp3nd762MAO283N"
#iv=b"This is an IV456"
iv=Random.new().read(ARC2.block_size)
print("Block Size: ",ARC2.block_size)

#message=b'A really secret message. Not for prying eyes.'
for i in range (8):
	f=open('ciphertext_1mb.txt',encoding="ANSI")
	inp=f.read()
	message='null'
	for j in range(2**i):
		message+=inp
	output.write(i+1,0,round(len(message)/(1024*1024)))
	print("Message size(mb): ", len(message)/(1024*1024))
	message=str.encode(message)
	cipher_text,time_enc=encryption(message)
	plain_text,time_dec=decryption(cipher_text)	
	print(message==plain_text)
	#print("Message size(mb): ", len(message)/(1024*1024))
	print("Cipher text size(mb): ",len(cipher_text)/(1024*1024))
	print("\n\n")
	output.write(i+1,1,time_enc)
	output.write(i+1,2,time_dec)
	output.write(i+1,3,len(cipher_text)/(1024*1024))

wb.save('ARC2.xls')


#print(plain_text)

#print(timeit.timeit(encryption))