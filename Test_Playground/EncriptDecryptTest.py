import sys
sys.path.append("/3D-Encrypt")
# sys.path.append("/Crypto")
import numpy as np
import Utils as util
import open3d as o3d

dat = util.get_mesh('encrypt_rabbit.ply')
ar = np.array([[0.1111,0.2222,0.3333],[0.4444,0.5555,0.6666],[0.7777,0.8888,0.9999]])
tri = np.array([[0,1,2]])
dat.vertices = util.get_vertices_vector(ar)
dat.triangles = util.get_triangle_vector(tri)
# print(util.get_vertices_ndarray(dat))
mat,k = util.encrypt_mesh(dat,bit_length=16,rangee=6189)

# print(util.get_vertices_ndarray(mat))

mat_d = util.decrypt_mesh(mat,k,rangee=6189)

print(util.get_vertices_ndarray(mat_d))
