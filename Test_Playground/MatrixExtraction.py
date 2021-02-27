import sys
sys.path.append("/3D-Encrypt")
import Utils as util

model = util.get_mesh('Model3D/bunny.tar/bunny/bunny/reconstruction/bun_zipper.ply')

vert_matrix = util.get_triangle_matrix(model)

print(vert_matrix)
print(vert_matrix.shape)


