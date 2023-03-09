from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from Utility.Utility import screw
from Utility.Utility import to_hex_string

data = 'secret data #00 secret data #00 '.encode()
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(data)
print('Initial:\n', to_hex_string(ciphertext))
error_ciphertext = screw(ciphertext, 1)
print('Screwed:\n', to_hex_string(error_ciphertext))

print('Deciphered initial:', cipher.decrypt(ciphertext))
print('Deciphered screwed:', cipher.decrypt(error_ciphertext))