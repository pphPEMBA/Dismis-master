from pyicloud import PyiCloudService
from pyicloud.exceptions import PyiCloudFailedLoginException
import yaml

from action.tts.text_to_speech import speak

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
ICLOUD_USERNAME = profile_data['iphone']['icloud_username']
ICLOUD_PASSWORD = profile_data['iphone']['icloud_password']




def find_iphone():
    try:
        api = PyiCloudService(ICLOUD_USERNAME, ICLOUD_PASSWORD)
    except PyiCloudFailedLoginException:
        speak("Invalid Username & Password")
        return

    # All Devices
    devices = api.devices

    # Just the iPhones
    iphones = []

    for device in devices:
        current = device.status()
        if "iPhone" in current['deviceDisplayName']:
            iphones.append(device)

    # The one to ring
    phone_to_ring = None

    if len(iphones) == 0:
        speak("No iPhones found in your account")
        return

    elif len(iphones) == 1:
        phone_to_ring = iphones[0]
        phone_to_ring.play_sound()
        speak("Sending ring command to the phone now")

    elif len(iphones) > 1:
        for phone in iphones:
            phone_to_ring = phone
            phone_to_ring.play_sound()
            speak("Sending ring command to the phone now")


def iphone_battery():
    try:
        api = PyiCloudService(ICLOUD_USERNAME, ICLOUD_PASSWORD)
    except PyiCloudFailedLoginException:
        speak("Invalid Username & Password")
        return

    # All Devices
    devices = api.devices

    # Just the iPhones
    iphones = []

    for device in devices:
        current = device.status()
        if "iPhone" in current['deviceDisplayName']:
            iphones.append(device)

    for phone in iphones:
        status = phone.status()
        battery = str(int(float(status['batteryLevel']) * 100))
        speak(battery + 'percent battery left in ' + status['name'])
