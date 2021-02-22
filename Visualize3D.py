import open3d as o3d

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
   