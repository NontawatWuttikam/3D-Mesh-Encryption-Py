import sys
sys.path.append("/3D-Encrypt")
# sys.path.append("/Crypto")
import numpy as np
import Utils as util
import open3d as o3d

from ecc.curve import Curve25519,miniCurve,E222,secp256k1,secp112r1,sect113r1,magma
from ecc.key import gen_keypair
from ecc.cipher import ElGamal
from ecc.curve import Point

import struct

value = 5.1254756

ba = bytearray(struct.pack("f", value)) 

# Plaintext
a = b"20121"
b = b"12"
c = b"13"
d = b"14"
e = b"15"
f = b"16"
plaintext = b
# Generate key pair
pri_key, pub_key = gen_keypair(secp112r1)
# pri_key = 2098162710
# pub_key = Point(x=1921128866, y=873348088, curve=magma)
print(pri_key)
print(pub_key)
# Encrypt using ElGamal algorithm
cipher_elg = ElGamal(secp112r1)
C1, C2 = cipher_elg.encrypt(a, pub_key)



# Decrypt
# C1.x = 5
new_plaintext = cipher_elg.decrypt(pri_key, C1, C2)



print(new_plaintext)
lla = 3229280735794148927415903955124721160015912325700291531873626230033157289810820461404903913144504876451816252806238181680507415752350932394680584694710242
# print(struct.unpack('f', new_plaintext))
# print(C1,C2)
a = '1001010101111110010010011101011101100000011011010000100000011011101111111011000011111001111110111001010000010000110000111010010111111001000001011100001011100011101001111100110010110111100100001011010111001101111110101001'
print(len(a))
# >> True