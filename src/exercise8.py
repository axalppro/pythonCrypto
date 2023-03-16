import hmac
from hashlib import sha224, pbkdf2_hmac
from Crypto.Hash import *
from random import random

from Crypto.Hash import SHA224
from Crypto.Random import get_random_bytes

from Utility.Utility import *

NUMBER_OF_FILES = 4

key = get_random_bytes(16)

plaintext1 = b'He will be known as King'
hmac_text1 = hmac.new(key, plaintext1, SHA224)

# Concatenate two bytes objects in a file
to_file('with_hash_original.bin', hmac_text1.digest(), plaintext1)

# Read bytes_1 and bytes_2 in a file
bytes_1, bytes_2 = from_file('with_hash_original.bin', 28)
print(bytes_1)
print(bytes_2)

#Copying files with errors
for i in range(NUMBER_OF_FILES):
    error = int((random()*10) % 5)
    name = "with_hash%d"%i
    screw_file('with_hash_original.bin', name, error)
    print(name + '  errors: ' + str(error))

print(str(NUMBER_OF_FILES) + ' files generated\n')

#Analysing files
for i in range(NUMBER_OF_FILES):
    name = "with_hash%d"%i
    bytes_1, bytes_2 = from_file(name, 28)
    if bytes_1 == hmac.new(key, bytes_2, SHA224).digest():
        print(name + ' is valid')
    else:
        print(name + 'is not valid')

