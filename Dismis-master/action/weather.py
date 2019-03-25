import pywapi
from action.tts.text_to_speech import speak


def weather(city_name, city_zip):
    weather_com_result = pywapi.get_weather_from_weather_com(city_zip, units="imperial")
    weather_result = "Weather.com says: It is " \
                     + weather_com_result['current_conditions']['text'].lower() \
                     + " and " + weather_com_result['current_conditions']['temperature']  \
                     + " degree farenheit now in " + city_name
    speak(weather_result)


