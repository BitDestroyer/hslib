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
How to find an all devices matching a portion of the device name, room, or by floor
"""
# name = input("Enter a Device name: ")
# floor = input("Enter a Device floor: ")
# room = input("Enter a Device room: ")
#
# print("searching for name: ", name + " and room: ", room + " and floor: ", floor)
# result = devices.find_devices(name=name, floor=floor, room=room)
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
name = input("Enter a Device name: ")
device = devices.find_exact_device(name)
print(device)

devices.turn_off(name)
print(device)

"""
Update all devices whose status have changed since last update
"""
# devices.update_all_devices()

"""
this is a sample of automating through usage of the libraries functions
"""
# def motion_has_changed(device):
#     temperature = devices.find_devices(name='Ambient Temperature', room="apartment")[0]
#     light = devices.find_exact_device("apt1")
#     print("motion has changed, it is now: {} it is about {} degrees in the apartment".format(device.status, temperature.value))
#     if device.status == "Motion":
#         devices.turn_on(light.name)
#     else:
#         devices.turn_off(light.name)
#
#
# motion = devices.find_devices(name="Home Security", room="Apartment")[0]
# motion.callback = motion_has_changed
# while True:
#     time.sleep(1)
#     devices.update_all_devices()
