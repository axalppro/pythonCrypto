from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Utility.Utility import *

BLOCK_SIZE = 16

plaintext = 'He will be known as King Charles III. That was the first decision of the new king\'s reign.' \
            'He could have chosen from any of his four names - Charles Philip Arthur George.'.encode()

padded_plaintext = pad(plaintext, BLOCK_SIZE)
unpadded_plaintext = unpad(padded_plaintext, BLOCK_SIZE)

print('PLain text\t\t' + str(plaintext))
print('Padded text\t\t' + str(padded_plaintext))
print('Unpadded text\t' + str(unpadded_plaintext))
