import requests
from action.tts.text_to_speech import speak
import time
from bs4 import BeautifulSoup
import re
import feedparser



def top_google_news():
    speak('sure sir')
    url = 'http://news.google.com/news?pz=1&cf=all&ned=in&hl=en&output=rss'
    feed = feedparser.parse(url)
    print("Here is the headline news")
    speak("Here is the headline news")
    for post in feed.entries:
        print(post.title)
        speak(post.title)
       
# USA news
def us_news():
    speak('got it sir')
    contents = requests.get(
        "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ace7c1fca4544f4f8b0bd6a31888e7d5").json()
    articles = contents['articles']
    count = 0
    speak('Here is the headlines news')
    for article in articles:
        print(article['title'] + article['content'])
        speak(article['title'] + article['content'])
        count += 1
        time.sleep(1)

        if (count == 3):
            break
            speak('done boss')







