from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

def aes(msg):
	key = get_random_bytes(16)
	text = msg.encode("UTF-8")
	text = pad(text, AES.block_size)

	enc = AES.new(key, AES.MODE_CBC)
	IV = enc.IV
	dec = AES.new(key, AES.MODE_CBC, IV=IV)

	ciphertext = enc.encrypt(text)
	plaintext = dec.decrypt(ciphertext)
	print(ciphertext)
	print(plaintext)


aes("AES CBC MODE")

