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
    task = Task("Digital Task", debug_mode=True)
    digital_device_name = "cDAQ1Mod1"
    channel_name="channel"
    print("Task name", task.name)
    NIDAQMXChannel =task.do_channels.add_do_chan(
                digital_device_name + "/port0",
                name_to_assign_to_lines=channel_name,
                line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    print("Channels:\t" + str(task.do_channels))
    print("Channels:\t" + str(task.channels))
    
def test_duty_cycle():
    task = Task("Digital Task", debug_mode=True)
    print("Task name", task.name)
    task.duty_cycle = 0.1
    while not task.is_task_done():
        print("Is task done?:\t" + str(task.is_task_done()))
    print("Is task done?:\t" + str(task.is_task_done()))
    task.stop()

def test_sampling_clock_configuration():
    task = Task("Digital Task", debug_mode=True)
    print("Task name", task.name)
    repeats = 1
    samples_per_frame = 50
    frames_per_s = 2
    samples_per_s = samples_per_frame * frames_per_s
    if (task.timing.cfg_samp_clk_timing(\
            samples_per_s,
            sample_mode=AcquisitionType.CONTINUOUS,
            samps_per_chan=samples_per_frame*repeats) == 0):
        print("Configured clock successfully")
    else:
        print("Clock not configured successfully")

def test_analog_task_creation():
    task = Task("Analog Task", debug_mode=True)
    print("Task name", task.name)
    analog_device_name = "cDAQ1Mod2"
    analog_channels = []
    mfc_flat_list = [1,0,2]
    for mfc in mfc_flat_list:
        analog_channels.append(mfc)
    for chan in analog_channels:
        ao = analog_device_name + "/ao%d" % chan
        task.ao_channels.add_ao_voltage_chan(ao)

if __name__ == "__main__":
    # test_device_creation()
    print("\n")
    test_digital_task_creation()
    print("\n")
    test_duty_cycle()
    print("\n")
    test_analog_task_creation()
    print("\n")
    test_sampling_clock_configuration()