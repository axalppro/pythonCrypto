from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

from Utility.Utility import bxor

BLOCK_SIZE = 16

plaintext1 = 'He will be known as King'.encode()
key = get_random_bytes(len(plaintext1))
print('text + key')
print(plaintext1)
print(key)

ciphertext1 = bxor(plaintext1, key)
print('result of xor')
print(ciphertext1)

dexored = bxor(ciphertext1, key)
print('dexored text')
print(dexored)

plaintext2 = "And she will be his queen".encode()
ciphertext2 = bxor(plaintext2, key)

#case of eve getting ciphertext1 and plaintext1
#if she knows both she just has to xor them to get the key and then she can decrypt ciphertext2

theSecretKey = bxor(ciphertext1, plaintext1)
hacked_text2 = bxor(ciphertext2, theSecretKey)
print('hacked text 2')
print(hacked_text2)