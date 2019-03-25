from selenium import webdriver
import re
import webbrowser
import time


from action.tts.text_to_speech import speak




    #speak('Aye aye captain, opening Firefox')
   

def open_website(voice_text):
    reg_ex = re.search('open (.+)', voice_text)
    if reg_ex:
        domain = reg_ex.group(1)
        speak('aye aye captain')
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)
        time.sleep(1.5)
        speak('Openned sir')
    else:
        speak('Network error')

def location(voice_text):
    data = voice_text.split(" ")
    location = ""
    location = location.split(" ")
    for i in range(2, len(data)):
        location.append(data[i])
    str1 = "  ".join(location)
    speak("Hold on sir, I will show you where " + str1 + " is.")
    webbrowser.open("https://www.google.nl/maps/place/" + str1)
    time.sleep(5)


def bookmark():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys("^d")
    print('Page bookmarked')
    speak("Page bookmarked")