import open3d as o3d
import numpy as np
import rsa
import copy
import numpy as np
from rsa.core import encrypt_int,decrypt_int
from scipy.fftpack import dct,idct

def encrypt_RSA(num,pubkey):
   """
   ## Ecrypt integer with public key generated

      input num: integer (the number to encrypt)
            pubkey: PublicKey (the publickey obj generated from rsa)
      
      output cypherInt (encrypted integer)

   """
   return encrypt_int((num.item()), pubkey.e, pubkey.n)

def decrypt_RSA(crypto,privkey):
   """
   ## Decrypt cypherInt with private key generated

      input cyrpto: integer (the cypherInt to decrypt)
            privkey: PrivateKey (private key object generated from rsa)
      
      output integer (decrypted integer)

   """
   return decrypt_int(crypto.item(), privkey.d, privkey.n)

def encrypt_ECC():
   return None

def decrypt_ECC():
   return None

def encrypt_tri_matrix(ndarray,bit_length):

   """
   ## Encrypt any ndarray (normally 3x3) using RSA algorithm piecewisely

      input ndarray: numpyArray (any NxN np array to encrypt)
            bit_length: integer (bit length for rsa key)
      
      output cypherArray (piecewise - encrypted ndarray)

   """

   res = []
   f = np.vectorize(encrypt_RSA)
   (pubkey, privkey) = rsa.newkeys(bit_length)
   for mat in ndarray:
      temp_mat = []
      for row in mat:
         temp_r = []
         for ele in row:
            temp_r.append(encrypt_RSA(ele,pubkey))
         temp_mat.append(temp_r)
      res.append(temp_mat)
   return np.array(res),privkey

def decrypt_tri_matrix(ndarray,privkey):
   """
   ## decrypt any ndarray (normally 3x3) using RSA algorithm piecewisely

      input ndarray: numpyArray (any NxN np array to encrypt)
            privkey: PrivateKey (private key object generated from rsa)
      
      output ndarray (piecewise - decrypted ndarray)

   """
   res = []
   for mat in ndarray:
      temp_mat = []
      for row in mat:
         temp_r = []
         for ele in row:
            temp_r.append(decrypt_RSA(ele,privkey))
         temp_mat.append(temp_r)
      res.append(temp_mat)
   return np.array(res)

def show_mesh_from_file(file,cvn=True):
   """
   ## show mesh from input path .ply

      input file: String (path string of .ply file)
            cvn: Boolean (calculate normal or not)

   """
   mesh = o3d.io.read_triangle_mesh(file)
   if cvn:
      mesh.compute_vertex_normals()
   o3d.visualization.draw_geometries([mesh]) 

def get_mesh(file):
   """
   ## get_mesh open3d object from file path

      input file: String (path string of .ply file)

      output mesh: TriangleMesh (mesh object)

   """
   return o3d.io.read_triangle_mesh(file)

def show_mesh(ar,cvn=True):
   """
   ## show mesh in multiple object

      input ar: List (a list of open3d mesh object for display)
            cvn: Boolean (calculate normal or not)
   """
   if cvn:
      for k,i in enumerate(ar):
         ar[k] = i.compute_vertex_normals()
   o3d.visualization.draw_geometries(ar) 

def get_vertices_ndarray(obj):
   """
   ## get vertice in ndarray from mesh object

      input obj: TriangleMesh (a TriangleMesh object)

      output vertices: ndarray (a numpy array of vertices) 
   """
   return np.asarray(obj.vertices)

def get_vertices_vector(ndarray):
   """
   ## get vertice in Vector3d from vertices ndarray

      input ndarray: ndarray (a numpy array of vertices)

      output vertices: Vector3dVector (a vector3d object of vertices)
   """
   return o3d.utility.Vector3dVector(ndarray)

def get_triangle_ndarray(obj):
   """
   ## get vertice in ndarray from mesh object

      input obj: TriangleMesh (a TriangleMesh object)

      output triangles: ndarray (a numpy array of trangles) 
   """
   return np.asarray(obj.triangles)

def get_triangle_vector(ndarray):
   """
   ## get vertice in Vector3d from vertices ndarray

      input ndarray: ndarray (a numpy array of triangles)

      output triangles: Vector3iVector (a vector3d object of triangle)
   """
   return o3d.utility.Vector3iVector(ndarray)

def get_triangle_matrix(obj):
   """
   ## get 3x3 triangle matrix from TriangleMesh object

      input obj: TriangleMesh (a Triangle Mesh object)

      output tri_matrix : ndarray(m,3,3) (an extracted triangle matrix)
             idx_matrix : ndarray(m,3) (index of each triangle matrix that mappped to vertices)

             ** m: integer (vertcices length)
   """
   tri = get_triangle_ndarray(obj)
   vert = get_vertices_ndarray(obj)

   matrix_set = []
   tri_matrix = np.array([[vert[i[0]], vert[i[1]], vert[i[2]]] for i in tri])
   idx_matrix = tri
   return tri_matrix,idx_matrix
   
def get_dct_coef_from_vertices(ndarray):
   """
   ## get dct coefficient from any 2d ndarray

      input ndarray : int ndarray(n,n) (a 2d ndarray)

      output dct: float ndarray(n,n) (a discrete cosine transform of 2d array)
   """
   return dct(ndarray)

def get_dct_coef_from_tri_matrix(ndarray):
   """
   ## get dct coefficient from any multiple 2d ndarray 

      input ndarray : int ndarray(m,n,n) (a 2d ndarray wth m triangle)

      output dct: float ndarray(m,n,n) (a discrete cosine transform of 2d array with m elements)
   """
   return np.array([dct(ar) for ar in ndarray])

def get_idct_from_coef(ndarray):
   """
   ## get idct coefficient from any multiple 2d ndarray 

      input ndarray : float ndarray(m,n,n) (a 2d ndarray wth m idct matrix)

      output idct: int ndarray(m,n,n) (a 2d idct matrix with m elements)
   """
   return np.array([idct(ar) for ar in ndarray])

def flaot_to_int_normalize_matrix(ndarray,r = 780):
   """
   ## normalize the (m,n,n) ndarray with m elements from float to integer

      input ndarray : float ndarray(m,n,n) (a 2d array with m elements in float space)
            **optional** r : integer (a mapping range from float to integer)

      output res: ndarray(m,n,n) (a 2d array with m elements in integer domain)
             minn : integer (min value of the float space in each m)
             maxx : integer (max value of the float space in each m)
             r : integer (a mapping range from float to integer)
   """
   minn = -1
   maxx = 1

   res = []
   f = np.vectorize(int)
   ro = np.vectorize(round)
   for mat in ndarray:
      t_r = (((mat - minn)/(maxx-minn))*r) + minn
      res.append(np.rint(t_r).astype(np.int64))
   
   print('min = ',np.min(res))
   return np.array(res), minn,maxx,r

def int_to_float_normalize_matrix(ndarray,r,minn,maxx):
   """
   ## normalize the (m,n,n) ndarray with m elements from float to integer

      input ndarray : ndarray(m,n,n) (a 2d array with m elements in integer domain)
            minn : integer (min value of the float space in each m)
            maxx : integer (max value of the float space in each m)
            r : integer (a mapping range from float to integer)

      output res: float ndarray(m,n,n) (a 2d array with m elements in float space)
   """
   res = []

   for mat in ndarray:
      t_r = (((mat - minn)/r)*(maxx-minn)) + minn
      res.append(t_r)
   
   return np.array(res)

def map_tri_matrix_to_vert_ar(ndarray, idxarray, old_vert):
   """
   ## map each 3*3 triangle matrix  with m elements to vertices array from given index.

      input ndarray : ndarray(m,3,3) (a 2d array with m elements of triangles)
            idxarray : ndarray(m,3) (a given index (old triangles ndarray) with m elemnents)
            old_vert : ndarray(m,3) (an old vertices object from the same mesh)

      output vert : ndarray(m,3) (a new verices object mapped from idx and tri matrix)
   """
   vert = old_vert.copy()
   for mat,idx in zip(ndarray,idxarray):
      for point, idex in zip(mat,idx):
         vert[idex] = point
   
   return vert

def random_vertice(ndarray):
   """
   ## random any ndarray in the right-most axis with numpy shuffle

      input ndarray : ndarray(m,3) (a 2d array with m elements of vertices)

      output vert : ndarray(m,3) (a shuffled ndarray)
   """
   return np.random.shuffle(ndarray)

def encrypt_mesh_RSA(mesh_,rangee=50, bit_length=128):
   """
   ## an encryption pipeline for RSA mesh encryption

      input mesh_ : TriangleMesh (a original mesh for encryption)
            rangee : integer (a mapping range for encryption proportional to quality)
            bit_length : integer (a bit length for encrytion proportional to computional cost and security)
            
      output mesh: TriangleMesh (an encrypted mesh)
             privkey: PrivateKey (a private key object for decryption)
      
      for the pipe line including:
         
         1. Deepcopy the mesh to another object (immuteable)

         2. Extract 3x3 Triangle Matrices from mesh

         3. In each matrices. find discrete cosine transform of 3x3 matrix to derive coef matrix.

         4. In each coef matrices. Map the flaot domain to integer domain

         5. In each mapped coef matrices. piecewisely encrypt each element in the matrices.

         6. Normalize the encrypted triangle matrix back to float.

         7. Map the 3x3 triangle matrix to 3x1 indexed triangle matrices.

         8. Convert ndarray of indexted triangle matrices to Vector3d object.

         9. Assign the Vector to the mesh.

         10. Return Mesh and privkey.
   """
   mesh = copy.deepcopy(mesh_)
   vert = get_vertices_ndarray(mesh)
   matrix,idx = get_triangle_matrix(mesh)
   dct_coef_tri = get_dct_coef_from_tri_matrix(matrix)
   dct_coef_tri_norm,minn,maxx,r = flaot_to_int_normalize_matrix(dct_coef_tri,r=rangee)
   dct_coef_tri_norm_encrypted,privkey = encrypt_tri_matrix(dct_coef_tri_norm,bit_length)
   print(dct_coef_tri_norm_encrypted)
   dct_coef_tri_inv = int_to_float_normalize_matrix(dct_coef_tri_norm_encrypted,r,minn,maxx)
   idct_mat = get_idct_from_coef(dct_coef_tri_inv)/6
   vert_new = map_tri_matrix_to_vert_ar(idct_mat,idx,vert)
   mesh.vertices = get_vertices_vector(vert_new)
   return mesh,privkey

def decrypt_mesh_RSA(mesh_,privkey,rangee=50):
   """
   ## an decryption pipeline for RSA mesh encryption

      input mesh_ : TriangleMesh (an encrypted mesh for encryption)
            rangee : integer (a mapping range for encryption proportional to quality)   
            pprivkey: PrivateKey (a private key object for decryption)

      output mesh: TriangleMesh (a decrypted mesh)       
   """
   mesh = copy.deepcopy(mesh_)
   vert = get_vertices_ndarray(mesh)
   matrix,idx = get_triangle_matrix(mesh)
   dct_coef_tri = get_dct_coef_from_tri_matrix(matrix)
   dct_coef_tri_norm,minn,maxx,r = flaot_to_int_normalize_matrix(dct_coef_tri,r=rangee)
   dct_coef_tri_norm_encrypted = decrypt_tri_matrix(dct_coef_tri_norm,privkey)
   dct_coef_tri_inv = int_to_float_normalize_matrix(dct_coef_tri_norm_encrypted,r,minn,maxx)
   idct_mat = get_idct_from_coef(dct_coef_tri_inv)/6
   vert_new = map_tri_matrix_to_vert_ar(idct_mat,idx,vert)
   mesh.vertices = get_vertices_vector(vert_new)
   return mesh

def save_mesh(name,mesh):
   """
   ## save a TriangleMesh objec to .ply

      input name : String (a string path and filename to save)
            mesh: TriangleMesh   
   """
   o3d.io.write_triangle_mesh(name, mesh)
   print("save",name,"successfully!")


