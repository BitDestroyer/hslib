import urllib.request
import json
import devices
import hstoken

base_url = "http://myhs.homeseer.com/JSON?token={}&".format(hstoken.secret)

def do_communication(http_request, data=None):
    """
    Make a request to HomeSeer and get the answer in JSON
    """
    with urllib.request.urlopen(http_request, data=data) as data_stream:
        raw_data = data_stream.read()

    json_data = json.loads(raw_data)
    return json_data


def load_devices(ref='all'):
    req = base_url + "request=getstatus&ref={}".format(ref)
    json_data = do_communication(req)
    devices_json = json_data.get('Devices')

    for dev in devices_json:
        devices.add_device(dev)


def set_device(ref, value):
    req = base_url + "request=controldevicebyvalue&ref={}&value={}".format(ref, value)
    response = do_communication(req)


def update_all_devices(id):
    req = base_url + "request=getdeviceschanged&devicechangeid={}".format(id)
    json_data = do_communication(req)
    devices_list = json_data.get('refs')

    return devices_list
