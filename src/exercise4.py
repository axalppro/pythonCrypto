import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

data = b"secret"
key = get_random_bytes(16)
cipher1 = AES.new(key, AES.MODE_CBC)
cipher2 = AES.new(key, AES.MODE_CBC)
ct_bytes1 = cipher1.encrypt(pad(data, AES.block_size))
ct_bytes2 = cipher2.encrypt(pad(data, AES.block_size))

iv1 = b64encode(cipher1.iv).decode('utf-8')
ct1 = b64encode(ct_bytes1).decode('utf-8')

iv2 = b64encode(cipher2.iv).decode('utf-8')
ct2 = b64encode(ct_bytes2).decode('utf-8')

result1 = json.dumps({'iv':iv1, 'ciphertext':ct1})
result2 = json.dumps({'iv':iv2, 'ciphertext':ct2})

print(result1)
print(result2)

decipher1 = AES.new(key, AES.MODE_CBC, cipher1.iv)
decipher2 = AES.new(key, AES.MODE_CBC, cipher2.iv)
decrypted1 = unpad(decipher1.decrypt(ct_bytes1), AES.block_size)
decrypted2 = unpad(decipher2.decrypt(ct_bytes2), AES.block_size)
print(decrypted1)
print(decrypted2)


