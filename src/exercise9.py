import hmac
from hashlib import sha224, pbkdf2_hmac

from Crypto.Cipher import AES
from Crypto.Hash import *
from random import random

from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

from Utility.Utility import *

NUMBER_OF_FILES = 4

key = get_random_bytes(16)

plaintext1 = b'He will be known as King'
cipher1 = AES.new(key, AES.MODE_CBC)
ct_bytes1 = cipher1.encrypt(pad(plaintext1, AES.block_size))
hmac_text1 = hmac.new(key, ct_bytes1, SHA256)

# Concatenate two bytes objects in a file
to_file('hash_then_mac.bin', hmac_text1.digest(), ct_bytes1)

# Read bytes_1 and bytes_2 in a file
bytes_1, bytes_2 = from_file('hash_then_mac.bin', 32)
print(bytes_1.hex())
print(bytes_2.hex())

if bytes_1 == hmac.new(key, bytes_2, SHA256).digest():
    print('File 1 is integer')
else:
    print('File 1 corrupted')

screw_file('hash_then_mac.bin', 'hash_then_mac_error.bin', 8)

# Read bytes_1 and bytes_2 in a file
bytes_3, bytes_4 = from_file('hash_then_mac_error.bin', 32)
print(bytes_3.hex())
print(bytes_4.hex())

if bytes_3 == hmac.new(key, bytes_4, SHA256).digest():
    print('File 2 is integer')
else:
    print('File 2 corrupted')
