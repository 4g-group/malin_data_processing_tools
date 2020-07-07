#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rosbag  # to read rosbag file
import sys
import getopt
import csv  # to register rosbag in csv format
import shutil  # for file management, copy file
import os  # for file management make directory


def write2csv(bag_path, topics):
    bag = rosbag.Bag(bag_path)
    bagContents = bag.read_messages(topics)
    # create a new directory
    folder = bag_path.rstrip(".bag") + "_csv"
    try:  # else already exists
        os.makedirs(folder)
    except:
        print("UNEXPECTED ERROR: Make dir %s" % sys.exc_info())
    shutil.copyfile(bag_path, folder + '/' + bag_path.split("/")[-1])

    for topicName in topics:
        # Create a new CSV file for each topic
        filename = folder + '/' + topicName.replace('/', '_slash_') + '.csv'
        with open(filename, 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            firstIteration = True  # allows header row
            for subtopic, msg, t in bag.read_messages(topicName):  # for each instant in time that has data for topicName
                # parse data from this instant, which is of the form of multiple lines of "Name: value\n"
                # - put it in the form of a list of 2-element lists
                msgString = str(msg)
                msgList = msgString.split('\n')
                instantaneousListOfData = []
                for nameValuePair in msgList:
                    splitPair = nameValuePair.split(':')
                    for n in splitPair:
                        # remove leading white space
                        n.strip()
                    instantaneousListOfData.append(splitPair)

                # write the first row from the first element of each pair
                if firstIteration:  # header
                    headers = ["rosbagTimestamp"]  # first column header
                    for pair in instantaneousListOfData:
                        headers.append(pair[0])
                    filewriter.writerow(headers)
                    firstIteration = False
                # write the value from each pair to the file
                values = [str(t)]  # first column will have rosbag timestamp
                for pair in instantaneousListOfData:
                    if len(pair) > 1:
                        values.append(pair[1])
                    else:
                        values.append('')
                filewriter.writerow(values)
    bag.close()
    print("Done reading all")

def usage():
    print('./Bag2csv.py -b BAG_PATH -t TOPIC_1 TOPIC_2 ...')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:t:", ['help', 'bagpath=', 'topic='])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    topics = []
    bag_path = ''

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('./Bag2csv.py -b BAG_PATH -t TOPIC_1 TOPIC_2 ...')
            sys.exit()
        elif opt in ("-b", "--bagpath"):
            bag_path = arg
            print('Bag file :', bag_path)
        elif opt in ("-t", "--bagpath"):
            topics.append(arg)
            for a in args:
                topics.append(a)
            print('Topics :', topics)
        else:
            assert False, "Unhandled option"

    if bag_path != '' and len(topics) > 0:
        write2csv(bag_path, topics)
    elif bag_path == '':
        print("ERROR: NO PATH TO BAG")
        usage()
        sys.exit(2)
    elif len(topics) == 0:
        print("ERROR: TOPICS EMPTY")
        usage()
        sys.exit(2)

if __name__ == '__main__':
    main()
