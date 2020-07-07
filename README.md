# BagViz

## Bag2csv to transform a rosbag into csv files.
It needs python2 and python-rospy, test by trying to import rosbag in a python shell :

`python Bag2csv.py nom_du_bag.bag`

it will create several files (one for each topic), with headers.

## republish_cam_decompressed_topics.launch 
Launch file to republish available camera's topics as decompressed data.

replay compressed data and roslaunch launch file to decompressed available topics:
```
rosbag play compressed_clip.bag
roslaunch republish_cam_decompressed_topics.launch
```

Following topics will be available:
```
/camera/depth/image_rect_raw
/camera/infra1/image_rect_raw
/camera/infra2/image_rect_raw
```
