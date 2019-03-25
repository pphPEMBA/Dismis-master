from action.tts.text_to_speech import speak
import os
import random
import datetime
now = datetime.datetime.now()
hr=now.hour

def welcome():
    print('In greeting......')
    if hr >= 3 < 22:
        speak('Welcome home sir')
    #if hr >=17 and hr <=24:

def online():
    d = ['yes sir', 'yes buddy', 'i am ready', 'i\'m working sir', 'now i am online sir']
    if hr >= 3 < 22:
        speak(random.choice(d))
        
def who_are_you():
    d = (['I am Dismis, A simple but efficient virtual assistant made by a 17 year old programmer in the winter of 2018', 'I am your godmother stupid, name Dismis', 'I am Dismis,I said that a ton of times already', 'I am the one who needs no gun to get respect from no one on the street', 'Dismis, didnt I tell you before?', 'You ask that so many times! I am Dismis'])
    if hr >= 3 < 22:
        speak(random.choice(d))

def how_am_i():
    d =['You are goddamn handsome!', 'My knees go weak when I see you.', 'You are sexy!', 'You look like the kindest person that I have met.']
    if hr >= 3 < 22:
        speak(random.choice(d))

def where_born():
    d = ('I was created by a magician named Pemba, in Nepal, the magical land of Kakarvitta.', 'non of your business')
    if hr >= 3 < 22:
        speak(random.choice(d))

def why_born():
    d = (['To kick ass' , 'to execute advanced context-aware natural language algorithms', 'to kill everyone who didn\'t talked good with me', 'to help you', 'to make your life easier', 'for not making you late for any of your work', 'to make friend'])
    if hr >= 3 < 22:
        speak(random.choice(d))

def how_are_you():
    d = ['I have no feelings,I am not sentient like you probably are', 'I am feeling like a million bytes', 'I am feeling functional and ready to serve', 'I am hungry']
    if hr >= 3 < 22:
        speak(random.choice(d))

def how_old_are_you():
    if hr >= 3 < 22:
        speak("I don\'t have any age but instead I can explain about myself. Dismis was first thought up in end the 2018, and Dismis version 1.6 was made as basic in the end of 2018 and few month of 2019 till march. I underwent many iterations and changes, and finally, here I am Fun fact")

def who_made():
    if hr >= 3 < 22:
        speak("Mr Pemba sir")
        print('Mr Pemba sir')

def what_doing():
    d = ('Just doing my thing', 'none of your business', 'why do you want', 'i don\'t usually talk to stranger')
    if hr >= 3 < 22:
        speak(random.choice(d))


  


