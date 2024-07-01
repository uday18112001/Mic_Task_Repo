import speech_recognition as sr
import pygame
from gtts import gTTS
import random
import webbrowser
import os
import time

class Person:
    name = ''
    def set_name(self, name):
        self.name = name

def there_exist(terms, voice_data):
    for term in terms:
        if term in voice_data:
            return True
    return False

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not understand that')
        except sr.RequestError:
            speak('Sorry, the service is down')

        print(f">> {voice_data.lower()}")
        return voice_data.lower()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 100)
    audio_file = f'audio{r}.mp3'
    tts.save(audio_file)
    time.sleep(1)  # Add delay to ensure the file is saved

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    print(f"alexa: {audio_string}")

    try:
        os.remove(audio_file)
    except Exception as e:
        print(f"Error deleting audio file: {e}")

def respond(voice_data):
    person_obj = Person()  # Instantiate person object if needed

    # 1: Greeting
    if there_exist(['hey', 'hi', 'hello'], voice_data):
        greetings = [f"Hey, how can I help you {person_obj.name}?",
                     f"Hey, what's up? {person_obj.name}",
                     f"I am listening, {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings)-1)]
        speak(greet)

    # 2: Name
    if there_exist(["what is your name", "whats ur name", "tell me your name"], voice_data):
        if person_obj.name:
            speak("My name is Alexa")
        else:
            speak("My name is Alexa, what's your name?")

    if there_exist(["my name is"], voice_data):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"Okay, I will remember that {person_name}")
        person_obj.set_name(person_name)

    # 3: Greeting
    if there_exist(["how are you", "how are you doing"], voice_data):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: Search Google
    if there_exist(["search for"], voice_data) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1].strip()
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f"Here is what I found for {search_term} on Google")

    # 5: Search YouTube
    if there_exist(["youtube"], voice_data):
        search_term = voice_data.split("for")[-1].strip()
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f"Here is what I found for {search_term} on YouTube")

    # 6: Exit
    if there_exist(["exit", "quit", "goodbye"], voice_data):
        speak("Going offline")
        exit()

person_obj = Person()
while True:
    voice_data = record_audio()
    respond(voice_data)
