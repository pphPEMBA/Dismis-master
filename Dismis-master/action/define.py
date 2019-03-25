import wikipedia
from action.tts.text_to_speech import speak
import re
import wolframalpha

def define(voice_text):
    reg_ex = re.search('dismiss(.+)', voice_text)
    if reg_ex:
        domain = reg_ex.group(1)
        try:
            # wolfram Alfa
            
            app_id = "Q6Y3UQ-6T4J3423V7"
            client = wolframalpha.Client(app_id)
            res = client.query(domain)
            answer = next(res.results).text
            speak('wait a minute sir')
            print (answer)
            speak(answer)

        except:
            #wikipedia
            speak('wait a minute sir')
            print(wikipedia.summary(domain, sentences=2))
            speak(wikipedia.summary(domain, sentences=2))
