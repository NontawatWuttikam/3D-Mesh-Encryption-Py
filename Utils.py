import open3d as o3d
import numpy as np
from scipy.fftpack import dct,idct
import rsa
import copy
from rsa.core import encrypt_int,decrypt_int

import numpy as np

def encrypt(num,pubkey):
   return encrypt_int(int(num), pubkey.e, pubkey.n)

def decrypt(crypto,privkey):
   return decrypt_int(crypto, privkey.d, privkey.n)

def encrypt_tri_matrix(ndarray,bit_length):
   # res = []
   # f = np.vectorize(encrypt)
   # (pubkey, privkey) = rsa.newkeys(bit_length)
   # for mat in ndarray:
   #    res.append(f(mat,pubkey))
   # return np.array(res),privkey
   res = []
   f = np.vectorize(encrypt)
   (pubkey, privkey) = rsa.newkeys(bit_length)
   for mat in ndarray:
      temp_mat = []
      for row in mat:
         temp_r = []
         for ele in row:
            temp_r.append(encrypt(ele,privkey))
         temp_mat.append(temp_r)
      res.append(temp_mat)
   return np.array(res),privkey

def decrypt_tri_matrix(ndarray,privkey):
   res = []
   f = np.vectorize(decrypt)
   for mat in ndarray:
      res.append(f(mat,privkey))
   return np.array(res)

def show_mesh_from_file(file,cvn=True):
   mesh = o3d.io.read_triangle_mesh(file)
   if cvn:
      mesh.compute_vertex_normals()
   o3d.visualization.draw_geometries([mesh]) 

def get_mesh(file):
   return o3d.io.read_triangle_mesh(file)

def show_mesh(ar,cvn=True):
   if cvn:
      for k,i in enumerate(ar):
         ar[k] = i.compute_vertex_normals()
   o3d.visualization.draw_geometries(ar) 

def get_vertices_ndarray(obj):
   return np.asarray(obj.vertices)

def get_vertices_vector(ndarray):
   return o3d.utility.Vector3dVector(ndarray)

def get_triangle_ndarray(obj):
   return np.asarray(obj.triangles)

def get_triangle_vector(ndarray):
   return o3d.utility.Vector3iVector(ndarray)

def get_triangle_matrix(obj):
   tri = get_triangle_ndarray(obj)
   vert = get_vertices_ndarray(obj)

   matrix_set = []
   tri_matrix = np.array([[vert[i[0]], vert[i[1]], vert[i[2]]] for i in tri])
   idx_matrix = tri
   return tri_matrix,idx_matrix
   
def get_dct_coef_from_vertices(ndarray):
   return dct(ndarray)

def get_dct_coef_from_tri_matrix(ndarray):
   return np.array([dct(ar) for ar in ndarray])

def get_idct_from_coef(ndarray):
   return np.array([idct(ar) for ar in ndarray])

def flaot_to_int_normalize_matrix(ndarray,r = 780):
   minn = np.min(ndarray)
   maxx = np.max(ndarray)

   res = []

   for mat in ndarray:
      t_r = (((mat - minn)/(maxx-minn))*r) + minn
      res.append(np.round(t_r).astype(np.int32))
   
   return np.array(res), minn,maxx,r

def int_to_float_normalize_matrix(ndarray,r,minn,maxx):

   res = []

   for mat in ndarray:
      t_r = (((mat - minn)/r)*(maxx-minn)) + minn
      res.append(t_r)
   
   return np.array(res)

def map_tri_matrix_to_vert_ar(ndarray, idxarray, old_vert):
   
   vert = old_vert.copy()
   for mat,idx in zip(ndarray,idxarray):
      for point, idex in zip(mat,idx):
         vert[idex] = point
   
   return vert

def random_vertice(ndarray):
   return np.random.shuffle(ndarray)

def encrypt_mesh(mesh_,rangee=50, bit_length=128):
   mesh = copy.deepcopy(mesh_)
   vert = get_vertices_ndarray(mesh)
   matrix,idx = get_triangle_matrix(mesh)
   dct_coef_tri = get_dct_coef_from_tri_matrix(matrix)
   dct_coef_tri_norm,minn,maxx,r = flaot_to_int_normalize_matrix(dct_coef_tri,r=rangee)
   dct_coef_tri_norm_encrypted,privkey = encrypt_tri_matrix(dct_coef_tri_norm,bit_length)
   dct_coef_tri_inv = int_to_float_normalize_matrix(dct_coef_tri_norm_encrypted,r,minn,maxx)
   idct_mat = get_idct_from_coef(dct_coef_tri_inv)/6
   vert_new = map_tri_matrix_to_vert_ar(idct_mat,idx,vert)
   mesh.vertices = get_vertices_vector(vert_new)
   return mesh

def save_mesh(name,mesh):
   o3d.io.write_triangle_mesh(name, mesh)
   print("save",name,"successfully!")


