import requests
import json
from action.tts.text_to_speech import speak



def joke():
    res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if res.status_code == requests.codes.ok:
        print(res.json()["joke"])
        speak(str(res.json()["joke"]))
    else:
        speak("oops!I ran out of jokes")
