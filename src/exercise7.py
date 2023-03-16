from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

password = b'my super secret'
salt = get_random_bytes(16)
key = PBKDF2(password, salt, 32, count=10000, hmac_hash_module=SHA256)
print(key.hex())