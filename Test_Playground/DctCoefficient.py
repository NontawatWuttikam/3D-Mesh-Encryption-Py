import sys
sys.path.append("/3D-Encrypt")
# sys.path.append("/Crypto")
import numpy as np
import Utils as util
import open3d as o3d
import math
# model_ori = util.get_mesh('Model3D\dragon_recon.tar\dragon_recon\dragon_recon\dragon_vrip.ply')
model = util.get_mesh(r'D:\3D-Encrypt\Model3D\bunny.tar\bunny\bunny\reconstruction\bun_zipper.ply')

model_en,privkey,seed = util.encrypt_mesh_RSA(model,rangee=6189,bit_length=16)
util.save_mesh("encrypt_rabbit.ply", model_en)
model_dec = util.decrypt_mesh_RSA(model_en,privkey,4568125,rangee=6189)
en_mat,idx1 = util.get_triangle_matrix(model_en)
dec_mat,idx2 = util.get_triangle_matrix(model_dec)
en_mat = np.array(en_mat)
en_dec = np.array(dec_mat)

# entro_en = np.sum(util.local_entropy(en_mat))
# entro_dec = np.sum(util.local_entropy(dec_mat))

print('Entropy : ',util.calculate_entropy(model_en,privkey))
util.show_mesh([model_dec])

# print(entro_en)+

#Encrypt

# model_enc = util.get_mesh('encrpyt_rabbit.ply')
# util.show_mesh([model_enc])






