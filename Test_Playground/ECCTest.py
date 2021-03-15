# from ecpy.curves     import Curve,Point
# from ecpy.keys       import ECPublicKey, ECPrivateKey
# from ecpy.ecdsa      import ECDSA

# cv     = Curve.get_curve('secp256k1')
# pu_key = ECPublicKey(Point(0x65d5b8bf9ab1801c9f168d4815994ad35f1dcb6ae6c7a1a303966b677b813b00,

#                            0xe6b865e529b8ecbf71cf966e900477d49ced5846d7662dd2dd11ccd55c0aff7f,
#                            cv))
# pv_key = ECPrivateKey(0xfb26a4e75eec75544c0f44e937dcf5ee6355c7176600b9688c667e5c283b43c5,
#                       cv)


# signer = ECDSA()
# sig    = signer.sign(b'01234567890123456789012345678912',pv_key)
# assert(signer.verify(b'01234567890123456789012345678912',sig,pu_key))
from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from ecpy.curves     import Curve,Point
from ecpy.keys       import ECPublicKey, ECPrivateKey
from ecpy.ecdsa      import ECDSA

cv   = Curve.get_curve('secp256k1')
pu_key = ECPublicKey(Point(0x65d5b8bf9ab1801c9f168d4815994ad35f1dcb6ae6c7a1a303966b677b813b00,
                       0xe6b865e529b8ecbf71cf966e900477d49ced5846d7662dd2dd11ccd55c0aff7f,
                       cv))
pv_key = ECPrivateKey(123,
                  cv)

eth_k = generate_eth_key()
sk_hex = eth_k.to_hex()  # hex string
pk_hex = eth_k.public_key.to_hex()  # hex string
a = -92233720368547758085555555555555555555555555555
data = a.to_bytes(100,'big',signed= True)
# print(hex(pu_key.W.x)+''+hex(pu_key.W.y)[2:])
# print(hex(pu_key.W.x)+' '+hex(pu_key.W.y)[2:])


print(decrypt(sk_hex, encrypt(pk_hex, data)))
print(int.from_bytes(decrypt(sk_hex, encrypt(pk_hex, data)), 'big',signed = True))
# print(int(pk_hex, 16))
# print(pv_key.d)
# print(eth_k)
