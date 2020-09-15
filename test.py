import numpy as np
import os

basepath1 = 'data/170817_event_time/'

# events to contain a string of each of the event names of interest eg. ['gw200213']
events = []
times = []
for entry in os.listdir(basepath1):
    events.append(entry)
    with open(basepath1+entry, 'r') as f:
        times.append(np.float(f.readline()))

