# MALIN DATA PROCESSING TOOLS

## PLOC evaluation script
Check out https://github.com/4g-group/ploc_evaluation.git

## Bag2csv
### Prerequities
* Be sure to have python 2 on your computer
* Run the following command
```#bash
sudo apt-get install python-rosbag
```
### Usage
To use this application :
* Be sure to give execution right to the bag2csv.py file.
```#bash
chmod +x bag2csv.py
```
* if you want to know which topics are in the bag, just type the following command in a prompt :
```#bash
./bag2csv.py -b bag_file_path.bag -i
```
* if you already know which topics are of interests just enter the following command in a prompt :
```#bash
./bag2csv.py -b nom_du_bag.bag -t topic1 topic2
```
where topic1, topic2 corresponds to topics to convert in csv.
* if you do not know just want to extract all topics in a row enter the following command in a prompt :
```#bash
./bag2csv.py -b bag_file_path.bag
```

In both cases, it will create a folder next to the bag file which contains several csv files (one for each topic), with headers.

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

## Plot Data

We advise to use the amazing tool PlotJuggler to plot and vizualize data from a rosbag.
Github:
Website:

Here an example from our output bag file "E_scenario_cyborgloc_output.bag", You can see the trace from latitude and longitude data and the heading as a function of time.
![PlotJuggler example](https://github.com/4g-group/malin_data_processing_tools/plotjuggler_example_output.png)
