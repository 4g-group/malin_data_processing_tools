# MALIN DATA PROCESSING TOOLS

## PLOC evaluation script
Check out https://github.com/4g-group/ploc_evaluation.git

## bag2csv.py to transform a rosbag into csv files.

It needs python3-rosbag package.

example:
`./bag2csv.py -b bag_name.bag -t TOPIC1 TOPIC2`

It will create several files (one for each topic), with headers.
If no topic specified, all topics are converted.

## bagmerge.py

It needs python3-rosbag package.

example:
`./bagmerge.py main.bag to_merge.bag -o merged.bag`

It will create a "merged.bag" file in same folder.

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

