import hs_communication
import time

device_list = {}


class Device:
    def __init__(self, actual_device):
        self.name = None
        self.ref = None
        self.status = None
        self.actual_device = None
        self.value = None
        self.floor = None
        self.room = None
        self.update_device(actual_device)

    def update_device(self, device_info):
        self.name = device_info.get('name')
        self.ref = device_info.get('ref')
        self.status = device_info.get('status')
        self.value = device_info.get('value')
        self.floor = device_info.get('location2')
        self.room = device_info.get('location')
        self.actual_device = device_info

    def change_value(self, new_value):
        new_value = float(new_value)
        current_status = self.value

        if current_status != new_value:
            hs_communication.set_device(self.ref, new_value)
            while self.value == current_status:
                time.sleep(0.1)
                self.reload_device()

    def reload_device(self):
        hs_communication.load_devices(self.ref)

    def __str__(self):
        return 'Ref: {}, Name: {}, Status: {}, Current_Value: {}, Floor: {}, Room: {}'.format(
            self.ref, self.name, self.status, self.value, self.floor, self.room
        )


def add_device(dev):
    if dev.get('relationship') in [0, 2]:
        ref = dev.get('ref')
        if device_list.get(ref):
            device_list[ref].update_device(dev)
        else:
            device_list[ref] = Device(dev)


def reload_device_by_ref(ref):
    hs_communication.load_devices(ref)


def find_devices(name=None, room=None, floor=None):
    match_list = []

    if name == '':
        name = None

    if room == '':
        room = None

    if floor == '':
        floor = None

    for ref, device in device_list.items():
        name_matches = False
        room_matches = False
        floor_matches = False

        if not name or name.lower() in device.name.lower():
            name_matches = True

        if not room or room.lower() in device.room.lower():
            room_matches = True

        if not floor or floor.lower() in device.floor.lower():
            floor_matches = True

        if floor_matches and room_matches and name_matches:
            match_list.append(device)

    return match_list


def find_exact_device(name):
    name = name.lower()

    for ref, device in device_list.items():

        if device.name.lower() == name:
            return device


def turn_on(name):
    device = find_exact_device(name)

    if device is not None:
        device.change_value(254.0)

    else:
        print("could not find device, cannot perform turn_on")


def turn_off(name):
    device = find_exact_device(name)

    if device is not None:
        device.change_value(0.0)

    else:
        print("could not find device, cannot perform turn_off")


def update_all_devices():

    """
    This will get a list of devices that need to be updated and then update each one
    """
    update_ref_list = hs_communication.update_all_devices("doug_test")

    for ref in update_ref_list:
        reload_device_by_ref(ref)
