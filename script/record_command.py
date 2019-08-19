#!/usr/bin/env python3

# whill module example package
# Copyright (c) 2018 WHILL, Inc.
# This software is released under the MIT License.


import time
from datetime import datetime
from whill import ComWHILL


def log_command(pathname, front, side):
    with open(pathname, 'a') as f:
        f.write(f'{front},{side}\n')


whill = ComWHILL(port='COM5')
interval_msec = 1000
interval_sec = interval_msec / 1000

filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
pathname = f'data/{filename}.csv'
f = open(pathname, 'w')
f.close()

while True:
    command = input('Type command: ')

    if command == 'f':
        front = 100
        side = 0
    elif command == 'b':
        front = -100
        side = 0
    elif command == 'r':
        front = 0
        side = 75
    elif command == 'l':
        front = 0
        side = -75
    elif command == 's':
        front = 0
        side = 0
    else:
        break

    try:
        while True:
            print(front, side)
            whill.hold_joy(front, side, interval_msec)
            log_command(pathname, front, side)
            time.sleep(interval_sec)
    except:
        pass
