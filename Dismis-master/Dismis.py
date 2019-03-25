import speech_recognition as sr
import yaml
import sys
import datetime
import os

from brain import brain
from action.tts.text_to_speech import speak
from action import music


profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
city_code = str(profile_data['city_code'])
music_path = profile_data['music_path']
#access_token = profile_data['twitter']['access_token']
#access_token_secret = profile_data['twitter']['access_token_secret']
#consumer_key = profile_data['twitter']['consumer_key']
#consumer_secret = profile_data['twitter']['consumer_secret']
music.mp3gen(music_path)


print("  ________   __               __        ")
print(" |  _____  \(__)             (__)       ")
print(" | |     \  |__ ____ ___  ___ __ ____   ")
print(" | |      } |  / ___|   \/   |  / ___|  ")
print(" | |_____/  |  \___ \  |\/|  |  \___ \  ")
print(" |_________/|__/____/__|  |__|__/____/  ")

speak('Welcome Pemba sir, Dismis system is ready to run now')
now = datetime.datetime.now()
hr=now.hour
if hr < 12:
    print("Good moring boss. Have a nice day")
    speak("good moring boss. Have a nice day")
elif hr >= 12 and hr < 17:
    print("Good afternoon boss")
    speak("good afternoon boss")
elif hr >= 17 and hr <= 19:
    print("Good Evening boss")
    speak("good evening boss")

os.chdir('C:\\Users\\P.P.H PEMBA\\Desktop') #For win
#os.chdir('home/pi/Desktop')    #for linux

speech = sr.Recognizer()

def Dismis_is_listening():
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        speech.energy_threshhold = 4000
        print('listening.....')
        audio = speech.listen(source)
        voice_text = ''
        try:
            voice_text = speech.recognize_google(audio).lower().replace("'", "")
            print("DISMIS thinks you said " + voice_text)
            with open('speak.txt', mode='a+') as f1:
                f1.write(voice_text)
                f1.write('/n')

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print('Network error')
        brain(voice_text, music_path, city_name, city_code)

if __name__ == '__main__':

    while True:
        Dismis_is_listening()



