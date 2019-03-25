from horoscope_generator import HoroscopeGenerator
from action.tts.text_to_speech import speak


def tell_horoscope():

    print(HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence()))
    speak(HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence()))