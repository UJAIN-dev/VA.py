import pyttsx3
import sys
import speech_recognition as sr
import webbrowser
import os
from googlesearch import search
import keyboard
import platform
import time

# init pyttsx
engine = pyttsx3.init("sapi5") #The Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications
voices = engine.getProperty("voices") # engine.getProperty gives us voice samples

engine.setProperty('rate', 150) # Decrease the Speed Rate

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice

def speak(audio):
    engine.say(audio) # engine.say (listens to user input)
    engine.runAndWait() # engine.runAndWait

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say That Again Please...")
        return "None"
    return query

def greet():
    speak("Hey  There...       What is your name?")
    name = take_command().lower()
    speak("Hi " + name + " I    am    your   personal   search   engine   powered   by   google")

def searching():
    speak("So... What is it you want to look up in the internet")
    query = take_command()
    for j in search(query):
        print(j)

def exitormore():
    speak("You want to look up for something more... or exit?")
    command = take_command().lower()
    if command == "exit":
        speak("OK! Bye it was nice meeting you!")
        sys.exit()
    elif command == "more":
        searching()

if __name__ == '__main__':

    speak("Hi My Name Is Friday")
    speak("How can i be of your service")
    while True:
        query = take_command().lower()

        if 'play football' in query:
            speak("opening youtube")
            if platform.system() == "Darwin":
                webbrowser.get('macosx').open("https://youtube.com")
            elif platform.system() == "Windows":
                webbrowser.get('windows-default').open("https://youtube.com")

        elif 'open google search' in query:

            greet()
            searching()
            exitormore()

        elif 'open github' in query:
            speak("opening github")
            if platform.system() == "Darwin":
                webbrowser.get('macosx').open("https://github.com")
            elif platform.system() == "Windows":
                webbrowser.get('windows-default').open("https://github.com")

        elif 'open teams' in query:
            speak("opening teams")
            if platform.system() == "Darwin":
                os.system("open /Applications/Teams.app")
            elif platform.system() == "Windows":
                loc = os.path.join(os.environ['USERPROFILE'], "AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe")
                os.startfile(loc)

        elif 'play spotify' in query:
            platform.system()
            speak("opening spotify")
            if platform.system() == "Darwin":
                os.system("open /Applications/Spotify.app")
            elif platform.system() == "Windows":
                loc = os.path.join(os.environ['APPDATA'], "Spotify\\Spotify.exe")
                os.startfile(loc)
                time.sleep(1)
                keyboard.press_and_release('Space')

        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            if platform.system() == "Darwin":
                os.system("open /Applications/WhatsApp.app")
            elif platform.system() == "Windows":
                loc = os.path.join(os.environ['USERPROFILE'], "AppData\\Local\\WhatsApp\\WhatsApp.exe")
                os.startfile(loc)

        elif 'open music' in query:
            speak("opening music")
            webbrowser.get('windows-default').open("https://spotify.com")

        elif 'open disk c' in query:
            speak("Opening Local Disk C")
            webbrowser.get('windows-default').open("C://")

        elif 'open home' in query:
            if platform.system() == "Darwin":
                speak("Opening Home")
                webbrowser.open("/home/")
            else:
                speak("sorry only applicable in Mac OS devices ")

        elif 'exit' or 'bye' in query:
            if query == "exit":
                print("Exit")
                speak("OK! Bye it was nice meeting you!")
                exit(0)
            elif query == "bye":
                print("Bye")
                speak("OK! Bye it was nice meeting you!")
                exit(0)