import pyttsx3
import os
import sys

def speak(message):
     """
     This function takes a message as an argument and converts it to speech
    depending on the OS.
     """
     if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
     elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        return os.system(tts_engine + ' "' + message + '"') 
     elif sys.platform == 'win32':
         tts_engine = 'sapi5'
         engine = pyttsx3.init()
         voices = engine.getProperty('voices')       #getting details of current voice
         #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
         engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
         engine.say(message)
         engine.runAndWait()



