import time

from Crypto.Cipher import AES
from Crypto.Random import random
import binascii
exp_max = 18
max_key = pow(2, exp_max) - 1
plain_text = '0123456789012345'.encode() # type: bytes
secret_key = random.randrange(max_key)
print('The key to find by brute force is', secret_key)
#cipher
key = secret_key.to_bytes(32, byteorder='big') # key as bytes
cipher = AES.new(key, AES.MODE_ECB)
cipher_text = cipher.encrypt(plain_text)
print(binascii.hexlify(cipher_text))

#brute force attack
start_time = time.time()
print('Starting ')
for i in range(max_key):
    aKey = i.to_bytes(32, byteorder='big') # key as bytes
    decipher = AES.new(aKey, AES.MODE_ECB)
    deciphered_text = decipher.decrypt(cipher_text)
    if deciphered_text == plain_text:
        print('The key has been found in', round((time.time() - start_time),3), 's the text is :', deciphered_text)
        break;