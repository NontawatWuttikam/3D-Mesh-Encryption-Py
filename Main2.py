import Visualize3D as v3d
import numpy as np
import open3d

mesh = v3d.get_mesh("D:\\3D-Encrypt\\bunny.tar\\bunny\\bunny\\reconstruction\\bun_zipper.ply")

print(np.asarray(mesh.triangles))