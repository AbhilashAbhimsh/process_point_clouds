import open3d as o3d
# import numpy as np
import sys

if __name__ == "__main__":
    # get the pcd file to read
    point_cloud_path = sys.argv[1]
    # load the pcd file
    pcd = o3d.io.read_point_cloud(point_cloud_path)
    print("Initial points: {}".format(len(pcd.points)))
    # visualize the point cloud
    o3d.visualization.draw_geometries([pcd])

    # THIS TO SEE THE POINTS
    # print("{0}\nPoints\n{0}".format("*"*10))
    # np.set_printoptions(threshold=np.inf)
    # print(np.asarray(pcd.points))

    pcd = pcd.voxel_down_sample(voxel_size=0.2)
    print("Points after down sample: {}".format(len(pcd.points)))
    o3d.visualization.draw_geometries([pcd])
