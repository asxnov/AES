from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def aes_cfb(text, key):
#enc
	data = text.encode('utf-8')
	enc = AES.new(key, AES.MODE_CFB)
	cipher = enc.encrypt(data)
	iv = enc.iv
	ciphered_main = cipher

	print(ciphered_main)

#--------------------------------------------------
#dec
	dec = AES.new(key, AES.MODE_CFB, iv=iv)
	decipher = dec.decrypt(ciphered_main)
	decrypted_main = decipher.decode('utf-8')

	print(decrypted_main)

aes_cfb('Erbolat Asanov SIB 18', get_random_bytes(32))