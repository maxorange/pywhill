#!/usr/bin/env python3

# whill module example package
# Copyright (c) 2018 WHILL, Inc.
# This software is released under the MIT License.


import time
from whill import ComWHILL

whill = ComWHILL(port='COM5')
interval_msec = 1000
interval_sec = interval_msec / 1000

joys = []

with open('data/2019-08-15-04-31-45.csv', 'r') as f:
    line = f.readline()
    while line:
        joy = line.strip().split(',')
        joys.insert(0, joy)
        line = f.readline()

for joy in joys:
    print(joy)
    front = -1 * int(joy[0])
    side = -1 * int(joy[1])
    whill.hold_joy(front, side, interval_msec)
    time.sleep(interval_sec)
