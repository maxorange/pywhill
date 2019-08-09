#!/usr/bin/env python3

# whill module example package
# Copyright (c) 2018 WHILL, Inc.
# This software is released under the MIT License.


import time
from whill import ComWHILL

whill = ComWHILL(port='COM5')
result = whill.send_joystick(int(100), int(0))
# result = whill.send_power_on()
# result = whill.receive_data()
print(result)
