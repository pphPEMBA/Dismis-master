from action import date_time, define, jokes, quote, lets_talk, browser, date_time, notes, music, self_destruct,\
    news, find_iphone, horoscope, speedtest, system_status, system_task
import time
#from action.games.Hangman import hangman
from action import scissorpaperrock


def brain(voice_text, music_path, city_name, city_code):

    def check_message(check):
        """
         This function checks if the items in the list (specified in
        argument) are present in the user's input speech.
         """

        words_of_message = voice_text.split()


        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False


                #chatbot
    if check_message(['daddy\'s', 'home']) or check_message(['i', 'home']) or check_message(['daddys', 'home'])\
            or check_message(['i', 'here']) or check_message(['daddy', 'home']):
        lets_talk.welcome()
    elif check_message(['baby']) or check_message(['auntie']) or check_message(['aunty']) or check_message(['online']) \
            or check_message(['buddy']):
        lets_talk.online()
    elif check_message(['who', 'are', 'you']) or check_message(['introduce', 'yourself']) or check_message(['give', 'intro'])\
            or check_message(['tell', 'yourself']):
        lets_talk.who_are_you()
    elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
        lets_talk.how_am_i()
    elif check_message(['where', 'born']):
        lets_talk.where_born()
    elif check_message(['why','here']):
        lets_talk.why_born()
    elif check_message(['how','are']):
        lets_talk.how_are_you()
    elif check_message(['how', 'old', 'are', 'you'])or check_message(['what', 'age']) or check_message(['what\'s', 'age']) or \
            check_message(['whats', 'age']):
        lets_talk.how_old_are_you()
    elif check_message(['who', 'master']) or check_message(['who', 'coded']) or check_message(['who', 'made']):
        lets_talk.who_made()
    elif check_message(['what', 'doing']):
        lets_talk.what_doing()



            #action
    elif check_message(['what', 'date']) or check_message(['what\'s', 'date']) or check_message(['whats', 'date']) or check_message(['tell', 'date']):
        date_time.date()
    elif check_message(['what', 'time']) or check_message(['what\'s', 'time']) or check_message(['whats', 'time']) or check_message(['tell', 'time']):
        date_time.daytime()
    elif check_message(['set', 'timer']):
        date_time.timer()
    elif check_message(['start','stopwatch']):
        date_time.stopwatch2(voice_text)


    elif check_message(['dismiss']):
        define.define(voice_text)

        #not implement
    elif check_message(['sport']):
        games_sport.cricket()


    elif check_message(['tell', 'joke']) or check_message(['jokes']):
        jokes.joke()


    elif check_message(['play', 'music']) or check_message(['music']):
        music.play_random(music_path)
    elif check_message(['play']):
        music.play_specific_music(voice_text, music_path)
    elif check_message(['party', 'time']) or check_message(['party', 'mix']):
        music.play_shuffle(music_path)



    elif check_message(['stop']):
        music.stop(music_path)
    elif check_message(['restart']):
        music.restart(music_path)
    elif check_message(['pause']):
        music.pause(music_path)
    elif check_message(['forward']):
        music.forward(music_path)
    elif check_message(['rewind']):
        music.rewind(music_path)
    elif check_message(['volume', 'up']):
        music.volume_up(music_path)
    elif check_message(['volume', 'down']):
        music.volume_down(music_path)




    elif check_message(['take', 'note']):
        notes.note_something(voice_text)
    elif check_message(['show', 'notes']):
        notes.show_all_notes()


    elif check_message(['quote']):
        quote.quote()


    elif check_message(['usa', 'news']):
        news.us_news()
    elif check_message(['google', 'headlines']) or check_message(['google', 'news']):
        news.top_google_news()


    #elif check_message(['weather']):
        #weather.weather(city_name, city_code)


    elif check_message(['speed', 'test']) or check_message(['check', 'internet', 'speed']):
        speedtest.main()


    elif check_message(['open']):
        browser.open_website(voice_text)
    elif check_message(['where', 'is']):
        browser.location(voice_text)
    elif check_message(['bookmark', 'it']):
        browser.bookmark()


    elif check_message(['find','iphone']) or check_message(['ring', 'iphone']):
        find_iphone.find_iphone()
    elif check_message(['check', 'iphone' , 'battery']) or check_message(['tell','phone', 'battery']):
        find_iphone.iphone_battery()


    elif check_message(['tell', 'future']) or check_message(['how', 'future']) or check_message(['how','my', 'day']):
        horoscope.tell_horoscope()


    elif check_message(['blow', 'up', 'dismiss']) or check_message(['hate', 'dismiss']):
        self_destruct.self_destruct()


    elif check_message(['check', 'performance']) or check_message(['how', 'system']):
        system_status.system_status()
    elif check_message(['tell', 'up', 'time']):
        system_status.system_uptime()
    elif check_message(['reboot', 'system']):
        system_task.restart()
    elif check_message(['scissor', 'paper', 'rock']):
        scissorpaperrock.spr()

    
   