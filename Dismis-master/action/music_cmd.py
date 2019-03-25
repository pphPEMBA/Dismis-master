import os
from action.tts.text_to_speech import speak

def stop(music_path):
    os.system('mpg123 -q')
    speak('stopped sir')

def restart(music_path):
    os.system('mpg123 -b')
    speak('sure sir!')

def pause(music_path):
    os.system('mpg123 -s')
    speak('yes boss!')

def forward(music_path):
    os.system('mpg123 -.')

def rewind(music_path):
    os.system('mpg123 -,') 


def volume_up(music_path):
    os.system('mpg123 -+')

def volume_down(music_path):
    os.system('mpg123 --') 








