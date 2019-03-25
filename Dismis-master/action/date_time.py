from datetime import datetime
import time
from action.tts.text_to_speech import speak

def date():
    speak(time.strftime("%d %b %Y %A"))

def daytime():
    speak(time.strftime("%I:%M:%S %A"))

import time
import msvcrt

def stopwatch():
    x = input('Press s to start, p to pause, or r to reset: ')
    pause1 = 0.0
    pause2 = 0.0

    if x is 's':
        start = time.clock()
        x1 = 's'

        while True:
            if x is 'p':
                pause1 = time.clock() + pause1
                x = msvcrt.getwch()
                pause2 = time.clock() + pause2
                x1 = 'p'
            elif x is 'r':
                print('                         ', end='\r')
                print('0:0:0.00', end='\r')
                x = msvcrt.getwch()
                start = time.clock()
                pause1 = 0.0
                pause2 = 0.0
            elif x is 's':
                if msvcrt.kbhit():
                    x = msvcrt.getwch()
                else:
                    current = time.clock() - (start + (pause2 - pause1))
                    minutes = current / 60
                    seconds = current % 60
                    hours = minutes / 60
                    minutes = minutes % 60
                    a = str(int(hours))
                    b = str(int(minutes))
                    c = str(round(seconds, 2))
                    if float(c) < 0.02:
                        print('                         ', end='\r')
                    if(minutes < 10 and seconds < 10):
                        print(a + ':' + '0' + b + ':' + '0' + c, end='\r')
                    elif(minutes < 10):
                        print(a + ':' + '0' + b + ':' + c, end='\r')
                    elif(seconds < 10):
                        print(a + ':' + b + ':' + '0' + c, end='\r')
                    else:
                        print(a + ':' + b + ':' + c, end='\r')
                    x1 = 's'
            else:
                x = x1




import time
import msvcrt

def stopwatch2(voice_text):
    x = voice_text.split()
    pause1 = 0.0
    pause2 = 0.0

    if x is 's':
        start = time.clock()
        x1 = 's'

        while True:
            if x is 'pause':
                pause1 = time.clock() + pause1
                x = msvcrt.getwch()
                pause2 = time.clock() + pause2
                x1 = 'p'
            elif x is 'r':
                print('                         ', end='\r')
                print('0:0:0.00', end='\r')
                x = msvcrt.getwch()
                start = time.clock()
                pause1 = 0.0
                pause2 = 0.0
            elif x is 's':
                if msvcrt.kbhit():
                    x = msvcrt.getwch()
                else:
                    current = time.clock() - (start + (pause2 - pause1))
                    minutes = current / 60
                    seconds = current % 60
                    hours = minutes / 60
                    minutes = minutes % 60
                    a = str(int(hours))
                    b = str(int(minutes))
                    c = str(round(seconds, 2))
                    if float(c) < 0.02:
                        print('                         ', end='\r')
                    if(minutes < 10 and seconds < 10):
                        print(a + ':' + '0' + b + ':' + '0' + c, end='\r')
                    elif(minutes < 10):
                        print(a + ':' + '0' + b + ':' + c, end='\r')
                    elif(seconds < 10):
                        print(a + ':' + b + ':' + '0' + c, end='\r')
                    else:
                        print(a + ':' + b + ':' + c, end='\r')
                    x1 = 's'
            else:
                x = x1