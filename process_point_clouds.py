import open3d as o3d
# import numpy as np
import sys
from time import time

if __name__ == "__main__":
    # get the pcd file to read
    point_cloud_path = sys.argv[1]
    # load the pcd file
    pcd = o3d.io.read_point_cloud(point_cloud_path)
    # print("Initial points: {}".format(len(pcd.points)))

    # visualize the point cloud
    o3d.visualization.draw_geometries([pcd])

    # THIS TO SEE THE POINTS
    # print("{0}\nPoints\n{0}".format("*"*10))
    # np.set_printoptions(threshold=np.inf)
    # print(np.asarray(pcd.points))

    # DOWN_SAMPLE PCD
    pcd = pcd.voxel_down_sample(voxel_size=0.2)
    print("Points after down sample: {}".format(len(pcd.points)))
    # o3d.visualization.draw_geometries([pcd])

    # IMAGE_SEGMENTATION
    start_time = time()
    plane_model, inliers = pcd.segment_plane(distance_threshold=0.3, ransac_n=10, num_iterations=500)

    inlier_clouds = pcd.select_by_index(inliers)
    outlier_cloud = pcd.select_by_index(inliers, invert=True)

    inlier_clouds.paint_uniform_color([0, 1, 0])
    outlier_cloud.paint_uniform_color([1, 0, 0])

    print("The Segmentation Took {} seconds".format(time() - start_time))

    o3d.visualization.draw_geometries([inlier_clouds, outlier_cloud])

