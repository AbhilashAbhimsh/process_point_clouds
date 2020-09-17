Dependences:

python3
open3d 0.10.00
numpy
pandas
pptk
matplotlib

**Steps to Process LiDAR Data**
1. Capture the LiDAR data into a file
2. Process the File using any library of your choice
    Steps Involved in processing
    1. Down Sample the points in point clouds
       - Too Many Points we dont need, increases computation
    2. Define a region of interest
       - We want to basically detect objects/obstacle in some range, not the entire area where the LiDAR can emit lights
    3. Separate the Scene from Obstacles
       -The pcd might have data related to trees, roads, building which we are not interested , We are only interested mainly in cars, pedestrians, cyclist any object which might come in way of our car movement
       - Use any outlier detection algorithm to separate obstacles from the rest of the scene. Here I used RANSAC
    4. Once we get all points[related to Obstacles or referred as outliers], we need to cluster these points into a particular obstacle
       -There might of 100s of points pertaining to a single obstacle
    5. Put Bounding Boxes around the Obstacle[To Visualize]
3. After Completing processing, Show the Visualization of pcd with bounding boxes around the obstacles
