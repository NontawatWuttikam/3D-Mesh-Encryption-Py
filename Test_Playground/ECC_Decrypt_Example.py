import sys
sys.path.append("/3D-Encrypt")
# sys.path.append("/Crypto")
import numpy as np
import Utils as util
import open3d as o3d
import math
import threading
# model_ori = util.get_mesh('Model3D\dragon_recon.tar\dragon_recon\dragon_recon\dragon_vrip.ply')
model = util.get_mesh(r'D:\3D-Encrypt\encrypt_rabbit.ply')
import pickle
import sys
sys.path.append("/3D-Encrypt")
from ecc.curve import Point

with open("points.txt", "rb") as fp:   # Unpickling
    b = pickle.load(fp)

ar = []
for i in range(20):
    indice = i*50
    if indice > b.shape[0]:
        ar.append(b[i*50:])
        break
    ar.append(b[i*50:(i*50) + 50])
# result1 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (b,1586195138803258101888165091312624921523094064936772250442594853231) )   # evaluate "solve1(A)" asynchronously
# result2 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[1],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result3 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[2],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result4 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[3],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result5 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[4],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result6 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[5],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result7 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[6],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result8 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[7],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result9 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[8],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result10 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[9],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result11 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[10],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result12 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[11],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result13 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[12],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result14 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[13],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result15 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[14],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result16 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[15],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result17 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[16],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result18 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[17],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result19 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[18],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously
# result20 = threading.Thread(target = util.decrypt_tri_matrix_ECC, args = (ar[19],414641640772471910640348637261144273302333598097381382444927558241))    # evaluate "solve2(B)" asynchronously




# result1.start()
# result2.start()
# result3.start()
# result4.start()
# result5.start()
# result6.start()
# result7.start()
# result8.start()
# result9.start()
# result10.start()
# result11.start()
# result12.start()
# result13.start()
# result14.start()
# result15.start()
# result16.start()
# result17.start()
# result18.start()
# result19.start()
# result20.start()

# answer1 = result1.get(timeout=10)
# answer2 = result2.get(timeout=10)
model_en = util.decrypt_mesh_ECC(model,b,1586195138803258101888165091312624921523094064936772250442594853231)

util.show_mesh([model_en])






