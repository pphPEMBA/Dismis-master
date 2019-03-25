import sqlite3
from datetime import datetime
from action.tts.text_to_speech import speak

def note_something(speech_text):
    conn = sqlite3.connect('memory.db')
    words_of_message = speech_text.split()
    words_of_message.remove('note')
    cleaned_message = ' '.join(words_of_message)
    conn.execute("INSERT INTO notes (notes, notes_date) VALUES (?, ?)",
    (cleaned_message, datetime.strftime(datetime.now(), '%d-%m-%Y')))
    conn.commit()
    conn.close()
    speak('Your note has been saved.')


def show_all_notes():
    conn = sqlite3.connect('memory.db')
    speak('Your notes are as follows:')
    cursor = conn.execute("SELECT notes FROM notes")
    for row in cursor:
        speak(row[0])
    conn.close()
