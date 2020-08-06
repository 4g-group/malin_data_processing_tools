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

License
The MIT License

Copyright (c) 2012 William Woodall, John Harrison

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Authors
 @gmail.com  @gmail.com

Contact
 @sgme.com
