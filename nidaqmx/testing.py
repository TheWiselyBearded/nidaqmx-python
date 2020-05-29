import time
import datetime
import threading
import random
import collections
import numpy as np
import sys
from os import path
# sys.path.insert(0,path.abspath(path.join(path.dirname(__file__))))
# sys.path.insert(0,path.abspath(path.join(path.dirname("../"))))
# import nidaqmx
# print(sys.path)
import nidaqmx
from constants import (
LineGrouping, AcquisitionType)
from task import Task 

'''
TODO:
- Determine whether debug_mode can be a custom object 
with flags for printing additional text.
'''

def test_device_creation():
    print("Testing device creation")
    system = nidaqmx.system.System.local(True)
    for device in system.devices:
        if (device.debug_mode):
            print("Testing device return:\t" + str(device.name))

def test_digital_task_creation():
    print("Line grouping",LineGrouping.CHAN_FOR_ALL_LINES.value)
    task = Task("Digital Task", debug_mode=True)
    digital_device_name = "cDAQ1Mod1"
    channel_name="channel"
    print("Task name", task.name)
    NIDAQMXChannel =task.do_channels.add_do_chan(
                digital_device_name + "/port0",
                name_to_assign_to_lines=channel_name,
                line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    print("Channels:\t" + str(task.do_channels))

def test_analog_task_creation():
    task = Task("Analog Task", debug_mode=True)
    digital_device_name = "cDAQ1Mod1"
    channel_name="channel"
    print("Task name", task.name)
    # NIDAQMXChannel =task.do_channels.add_do_chan(
    #             digital_device_name + "/port0",
    #             name_to_assign_to_lines=channel_name,
    #             line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

if __name__ == "__main__":
    # print(sys.path)
    # test_device_creation()
    print("\n")
    test_digital_task_creation()
    # print("\n")
    # test_analog_task_creation()