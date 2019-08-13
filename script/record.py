#!/usr/bin/env python3

# whill module example package
# Copyright (c) 2018 WHILL, Inc.
# This software is released under the MIT License.

import time
from datetime import datetime
from whill import ComWHILL

whill = ComWHILL(port='COM5')
request_speed_mode = 0
interval_msec = 50
whill.start_data_stream(interval_msec, 0, request_speed_mode)

filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
pathname = f'data/{filename}.csv'
f = open(pathname, 'w')
f.close()

while True:
    print()
    time.sleep(interval_msec / 1000)
    is_refreshed = whill.refresh()
    if whill.latest_received_data_set == 0:
        # print('speed_profile:', whill.speed_profile[request_speed_mode])
        whill.start_data_stream(interval_msec, 1, request_speed_mode)
    else:
        level, current = whill.battery.values()
        # print('accelerometer:', whill.accelerometer)
        # print('gyro:', whill.gyro)
        print('joy:', whill.joy)
        # print('Battery Status: remaining capacity {level}%, current draiwng {current}mA'.format(level=level, current=current))
        # print('Motor Status')

        with open(pathname, 'a') as f:
            front = whill.joy['front']
            side = whill.joy['side']
            f.write(f'{front},{side}\n')

        request_speed_mode = (request_speed_mode + 1) % 6
        whill.start_data_stream(interval_msec, 0, request_speed_mode)

# while True:
#     time.sleep(interval_msec / 1000)
#     is_refreshed = whill.refresh()
#
#     print('joy:', whill.joy)
#     # print('Battery Status: remaining capacity {level}%, current draiwng {current}mA'.format(level=level, current=current))
#     # print('Motor Status')
#
#     with open(pathname, 'a') as f:
#         front = whill.joy['front']
#         side = whill.joy['side']
#         f.write(f'{front},{side}\n')
#
#     whill.start_data_stream(interval_msec, 0, request_speed_mode)
