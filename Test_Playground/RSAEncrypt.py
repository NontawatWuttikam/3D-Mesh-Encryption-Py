import rsa
from rsa.core import encrypt_int,decrypt_int

import numpy as np
(pubkey, privkey) = rsa.newkeys(128)

a = 3024
b = 1234

crypto = encrypt_int(a, pubkey.e, pubkey.n)
crypto = encrypt_int(b, pubkey.e, pubkey.n)

dec = decrypt_int(crypto, privkey.d, privkey.n)
print(crypto)
print(dec)


