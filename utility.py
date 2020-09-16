import open3d as o3d
import numpy as np
import struct
import sys

SIZE_OF_FLOAT = 4
# for point cloud type x,y,z,intensity
DEFAULT_FORMAT = 'ffff'


def convert_bin_pcd(bin_file_path, pcd_file_path):
    list_points = []
    with open(bin_file_path, 'rb') as f_obj:
        byte = f_obj.read(SIZE_OF_FLOAT*4)
        # Read all the data from bin file
        while byte:
            x, y, z, intensity = struct.unpack(DEFAULT_FORMAT, byte)
            list_points.append([x, y, z])
            byte = f_obj.read(SIZE_OF_FLOAT*4)
    # converting list to array
    np_list_points = np.asarray(list_points)
    # instantiating PointCloud class
    pcd = o3d.geometry.PointCloud()
    # vector class
    vector = o3d.utility.Vector3dVector
    # load all data to pcd obj
    pcd.points = vector(np_list_points)

    o3d.io.write_point_cloud(pcd_file_path, pcd)


if __name__ == "__main__":
    convert_bin_pcd(*sys.argv[1:])
