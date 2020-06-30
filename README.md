# hslib

This is a python library designed to control and update devices allowing for customized scripts or 3rd party applications to utilize the HomeSeer API.
 The library handles the json data from the HomeSeer API and retains a dictionary of the devices found there.
 Allowing the user to act on those device, using the built in device functions, can auto generate events that update and work in real time.
 This Library will require: Access to HomeSeer, either through a remote setup or access to a local set up.
 The library can access the API through either of the methods provided you have the IP address for a local set up or a token for remote set up.
 
 Ideally have atleast one device already set up in HomeSeer, but the library can run an update and add any devices that were not in HomeSeer before.

 ## Getting Started/installation
 Clone the Github #hslib repository
 uses python 3.7.7 please update if not
 
 ## Usage
 Samples are found in the program
 Import devices
 
 lights = device.find_device(ApartmentLights)
 
 if motion.status == "ON"
    device.turn_on(lights)

 
 
 ## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
 
