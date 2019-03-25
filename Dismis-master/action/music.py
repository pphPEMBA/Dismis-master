import os
import sys
import random
from action.tts.text_to_speech import speak



def mp3gen(music_path):
    """
    This function finds all the MP3 files in a folder and its subfolders and
    returns a list:
    """
    music_list = []
    for root, dirs, files in os.walk(music_path):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                music_list.append(os.path.join(root, filename.lower()))
    return music_list


def music_player(file_name):
    """
    This function takes the name of a music file as an argument and plays it
    depending on the OS.
    """
    if sys.platform == 'darwin':
        player = "afplay '" + file_name + "'"
        return os.system(player)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        player = "mpg123 '" + file_name + "'"
        return os.system(player)


def play_random(music_path):
    """
    Random music played.

    :param music_path:
    :return:
    """
    try:
        music_listing = mp3gen(music_path)
        music_playing = random.choice(music_listing)
        speak("Now playing: " + music_playing)
        music_player(music_playing)
    except IndexError as e:
        speak('No music files found.')
        print("No music files found: {0}".format(e))

def play_specific_music(speech_text, music_path):
    """
    User selected music played.

    :param speech_text:
    :param music_path:
    :return:
    """
    words_of_message = speech_text.split()
    words_of_message.remove('play')
    cleaned_message = ' '.join(words_of_message)
    music_listing = mp3gen(music_path)
    for i in range(0, len(music_listing)):
        if cleaned_message in music_listing[i]:
            music_player(music_listing[i])


def play_shuffle(music_path):
    try:
        music_listing = mp3gen(music_path)
        random.shuffle(music_listing)
        for i in range(0, len(music_listing)):
            music_player(music_listing[i])
    except IndexError as e:
        speak('No music files found.')
        print("No music files found: {0}".format(e))



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
