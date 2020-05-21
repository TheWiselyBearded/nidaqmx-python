import time
import datetime
import threading
import random
import collections
import numpy as np
from constants import (
    LineGrouping, AcquisitionType)
from _task_modules.do_channel_collection import DOChannelCollection
from task import Task 

def main():
    print("Line grouping",LineGrouping.CHAN_FOR_ALL_LINES.value)
    task = Task("task1", debug_mode=True)
    digital_device_name = "cDAQ1Mod1"
    channel_name="channel"
    print("Task name", task.name)
    # NIDAQMXChannel =task.do_channels.add_do_chan(
    #             digital_device_name + "/port0",
    #             name_to_assign_to_lines=channel_name,
    #             line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    # NIDAQMXChannel.do_num_lines = 32
    # print("\nNumber of lines:\t" + str(NIDAQMXChannel.do_num_lines) + \
    #              "\nChannel name:\t" + NIDAQMXChannel.name + \
    #              "\nTask name:\t" + task.name)

if __name__ == "__main__":
    main()