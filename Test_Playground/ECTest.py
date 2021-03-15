import sys
sys.path.append("/3D-Encrypt")
# sys.path.append("/Crypto")
import numpy as np
import Utils as util
import open3d as o3d
import EC as e

ecc = e.EC(105,307,120511)
g, _ = ecc.at(200)
e.ElGamal(ecc,g)
