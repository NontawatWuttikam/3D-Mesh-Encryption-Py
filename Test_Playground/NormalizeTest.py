import sys
sys.path.append("/3D-Encrypt")
# sys.path.append("/Crypto")
import numpy as np
import Utils as util
import open3d as o3d

dat = util.get_mesh('encrypt_rabbit.ply')
ar = np.array([[[0.1111,0.2222,0.3333],[0.4444,0.5555,0.6666],[0.7777,0.8888,0.9999]]])

norm,mi,ma,r = util.flaot_to_int_normalize_matrix(ar,6189)

print(norm)

un = util.int_to_float_normalize_matrix(norm,r,mi,ma)

print(un)

