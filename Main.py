import Visualize3D as v3d
import numpy as np
import open3d
# v3d.show_mesh_from_file("D:\\3D-Encrypt\\bunny.tar\\bunny\\bunny\\reconstruction\\bun_zipper.ply")

mesh = v3d.get_mesh("D:\\3D-Encrypt\\bunny.tar\\bunny\\bunny\\reconstruction\\bun_zipper.ply")
pcloud = open3d.io.read_point_cloud("D:\\3D-Encrypt\\bunny.tar\\bunny\\bunny\\reconstruction\\bun_zipper.ply")

mesh_jing = open3d.io.read_point_cloud("D:\\3D-Encrypt\\bunny.tar\\bunny\\bunny\\reconstruction\\bun_zipper.ply")
pc = v3d.get_mesh("D:\\3D-Encrypt\\pc.ply")
emp = open3d.utility.Vector3dVector(np.zeros((1,3)))
# mesh.vertices = emp
ver = open3d.utility.Vector3dVector(np.asarray(mesh.vertices)[:])
tri_n = np.asarray(mesh.triangles)[:]
l1 = tri_n[:int(tri_n.shape[0]//2)+1]
l2 = tri_n[int(tri_n.shape[0]//2):]
tri_n = np.vstack((l1,l2))
np.random.shuffle(tri_n)
np.random.shuffle(ver)

tri = open3d.utility.Vector3iVector(tri_n[:])
print(tri_n)
mesh.triangles = tri
mesh.vertices =ver



vert = np.asarray(mesh.vertices)
norm = np.asarray(mesh.vertex_normals)
print(np.asarray(mesh.vertices))

vert = vert[:]
pcd = open3d.geometry.PointCloud()
pcd.points = open3d.utility.Vector3dVector(vert)
pcd.normals = open3d.utility.Vector3dVector(norm)

# o3d.io.write_point_cloud("./data.ply", pcd)
# pcd.estimate_normals()


alpha = 0.3
distances = pcd.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 3 * avg_dist   

# radii = [0.005, 0.01, 0.02, 0.04]

# mesh_2 = open3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd, open3d.utility.DoubleVector([radius, radius * 2]))
# mesh_2.compute_vertex_normals()
# pc.compute_vertex_normals()
# mesh_jing.compute_vertex_normals()
mesh.compute_vertex_normals()
v3d.show_mesh([mesh],cvn=False)
tm = open3d.geometry.TriangleMesh(mesh.vertices,mesh.triangles)
print(tm)

p1 = np.asarray(pcd.points)
p2 = np.asarray(mesh_jing.points)

open3d.io.write_point_cloud("pc.ply", pcd)



