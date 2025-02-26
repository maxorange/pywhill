#!/usr/bin/env python3

# whill module example package
# Copyright (c) 2018 WHILL, Inc.
# This software is released under the MIT License.


import time
from whill import ComWHILL

whill = ComWHILL(port='COM5')
interval_msec = 1000
interval_sec = interval_msec / 1000

with open('data/2019-08-15-05-41-37.csv', 'r') as f:
    line = f.readline()
    while line:
        joy = list(map(int, line.strip().split(',')))
        print(joy)
        whill.hold_joy(int(joy[0]), int(joy[1]), interval_msec)
        time.sleep(interval_sec)
        line = f.readline()
