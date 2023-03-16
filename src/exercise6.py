from hashlib import sha224
from random import random

from Utility.Utility import *

NUMBER_OF_FILES = 4

plaintext1 = 'He will be known as King'.encode()
encodedtext1 = sha224(plaintext1).hexdigest().encode()

# Concatenate two bytes objects in a file
to_file('with_hash_original.bin', encodedtext1, plaintext1)

# Read bytes_1 and bytes_2 in a file
bytes_1, bytes_2 = from_file('with_hash_original.bin', len(encodedtext1))
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
    bytes_1, bytes_2 = from_file(name, len(encodedtext1))
    if bytes_1 == sha224(bytes_2).hexdigest().encode():
        print(name + ' is valid')
    else:
        print(name + 'is not valid')

