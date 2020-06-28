import urllib.request
import json
import hs_communication
import devices
import time

hs_communication.load_devices()

"""
How to find an exact device
"""
# name = input("Enter the exact Device name: ")
#
#
# result = devices.find_exact_device(name)
#
# for match in result:
#     print(match)


"""
How to find an all devices matching a portion of the device name
"""
# name = input("Enter a Device name: ")
#
#
# result = devices.find_devices(name)
#
# for match in result:
#     print(match)


"""
turn on a device
"""
# name = input("Enter a Device name: ")
# device = devices.find_exact_device(name)
# print(device)
#
# devices.turn_on(name)
# print(device)

"""
turn off a device
"""
# name = input("Enter a Device name: ")
# device = devices.find_exact_device(name)
# print(device)
#
# devices.turn_off(name)
# print(device)

"""
Update all devices whose status have changed since last update
"""
name = input("Enter a Device name: ")
devices.update_all_devices()
device = devices.find_exact_device(name)
print(device)
time.sleep(4)
devices.update_all_devices()
print(device)