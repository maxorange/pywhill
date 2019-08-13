#!/usr/bin/env python3

# whill module example package
# Copyright (c) 2018 WHILL, Inc.
# This software is released under the MIT License.


import time
from whill import ComWHILL

whill = ComWHILL(port='COM5')

whill.hold_joy(int(10), int(0))
# whill.unhold_joy()

# result = whill.send_power_on()
# result = whill.receive_data()
# print(result)

# while True:
#     whill.send_joystick(int(100), int(0))
#     time.sleep(1)

# whill.send_joystick(int(100), int(0))
