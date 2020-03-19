"""What is a Voice Assistant?
A voice assistant or intelligent personal assistant is a software agent that can perform tasks or services
for an individual based on verbal commands i.e. by interpreting human speech and respond via synthesized
voices. Users can ask their assistants’ questions, control home automation devices, and media playback via
voice, and manage other basic tasks such as email, to-do lists, open or close any application etc with verbal
 commands."""
#------------------------Personal Voice Assistant in Python------------------------
import pyttsx3
import datetime
# importing speech recognition package from google api
import speech_recognition as sr #-> speech_recognition – for recognizing the voice command and converting to text
import pyaudio  #-> pyaudio – for voice engine in python
import wikipedia
from time import ctime
import time
import os # to save/open files
import webbrowser
import googlesearch
from googlesearch import search
import re
# import pyowm  # current weather
# import smtplib  # email send module

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# speak any argument by this speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Hello sir. good Morning!")

    elif hour>=12 and hour<18:
        speak("Hello sir. good afternoon!")

    else:
        speak("Hello sir. Good evening!")

    speak("Hi'i am your assistant, What can i do for you ")

def takeCommand():

    # Record audio
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print('Listaning ....')
        r.pause_threshold =1
        audio = r.listen(source)

        # print("opening :" + r.recognize_google(audio))
        # p = r.recognize_google(audio)
        # webbrowser.open(p)

    query=""
    try:
        print('Recognizing....')
        # recording the audio using speech recognition
        query = r.recognize_google(audio, language='en-in')
        print(f'You said {query}\n')  #Google Speech Recognition could not understand audio
        #webbrowser.open(query) # user can say any query 
       # speak(query)
    # except Exception as e:
    except sr.UnknownValueError: 
        print("Say that again please....")
        return "None"
    return query

def Sofia(query):
    
    if "how are you" in query or "hi sofia" in query:
        speak("I am fine" or "i am great pretty")

    if "what is your name" in query:
        speak("my name is . but sofia don't no your name, you know ok")

    #Tells you the current time.
    #Sofia can you tell me the current time ? or “what is the time now ?”
    # and Sofia will tell you the current time of your timezone.
    if "what is time" in query or 'time' in query:
        # tyme= ctime() # print time 
        # print(tyme)
        speak(ctime())

    if "who are you" in query:
        speak("""Hello, I am sofia. Your personal Assistant.
        I am here to make your life easier. 
        You can command me to perform various tasks such as calculating sums or opening applications etcetra""")

def more_action(query):
    # name="Human"
    name="Dear"
    if "exit" in query or "bye" in query or 'bye sofia' in query:
        speak(f"ok bye {name}")
        exit()

# Driver Code
if __name__ == "__main__":
    wishMe()
    
    while True:
    #if 1:
    # function used to open application
    # present inside the system.
        query = takeCommand().lower()
        Sofia(query)
        more_action(query)
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "google" in query or 'google chrome' in query:
            webbrowser.open("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

        elif "open email" in query or "open my email" in query:
            webbrowser.open("https://mail.google.com/mail")
            

        elif "open stack overflow" in query or 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        #  Play you a song on VLC media player
        elif "play songs" in query or 'play music' in query:
            music_dir = "F:\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'video' in query:
            webbrowser.open('https://www.youtube.com/results?search_qurey=')
           

        
            #current weather
        # elif 'current weather' in query:
        #     reg_ex = re.search('current weather in (.*)', query)
        #     if reg_ex:
        #         city = reg_ex.group(1)
        #         owm = owm(API_key='here api key')
        #         obs = owm.weather_at_place(city)
        #         w = obs.get_weather()
        #         k = w.get_status()
        #         x = w.get_temperature(unit='celsius')
        #         speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
          