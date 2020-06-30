import urllib.request
import urllib.parse
import json
import devices
import hstoken

# if you are not using a token file, then change the URL to be your local HomeSeer's IP address.
# base_url = "http://my_local_ip_address/JSON?"
if hstoken.secret:
    base_url = "http://myhs.homeseer.com/JSON?token={}&".format(hstoken.secret)
else:
    base_url = "http://{}/JSON?".format(hstoken.ip_address)

if hstoken.username is not None:
    # install an authentication opener for URLs
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None,
                              base_url,
                              hstoken.username,
                              hstoken.password)

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    urllib.request.install_opener(urllib.request.build_opener(handler))


def do_communication(http_request, data=None):
    """
    Make a request to HomeSeer and get the answer in JSON
    """
    print("Accessing: ", http_request)
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
