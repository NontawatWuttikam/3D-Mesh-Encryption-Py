import sys
sys.path.append("/3D-Encrypt")
# sys.path.append("/Crypto")
import numpy as np
import Utils as util
import open3d as o3d
import math

a = np.array([[[0.1,0.2,0.3],[0.4,0.5,0.6],[0.7,0.8,0.9]],[[0.10,0.11,0.12],[0.13,0.14,0.15],[0.16,0.17,0.18]]])
a,minn,maxx,r = util.flaot_to_int_normalize_matrix(a,r=6189)
# a = a.flatten()
a, seed = util.shuffle(a)
a = util.int_to_float_normalize_matrix(a,r,minn,maxx)
a = util.unshuffle(a,seed)

# a = np.reshape(a,(2,3,3))
print(a)