import webbrowser
import os
import keyboard
import platform
import time
import pyttsx3
from chat_completetion import completion_api_call
# init pyttsx
engine = pyttsx3.init("sapi5") #The Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications
voices = engine.getProperty("voices") # engine.getProperty gives us voice samples

engine.setProperty('rate', 150) # Decrease the Speed Rate

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice

def speak(audio):
    engine.say(audio) # engine.say (listens to user input)
    engine.runAndWait() # engine.runAndWait



def take_action(keyword,query):

    if keyword == 'youtube':
    
        speak("opening youtube")

        if platform.system() == "Darwin":
            webbrowser.get('macosx').open("https://youtube.com")

        elif platform.system() == "Windows":
            webbrowser.get('windows-default').open("https://youtube.com")

    elif keyword == 'google':
        speak("opening Google")

        if platform.system() == "Darwin":
            webbrowser.get('macosx').open("https://google.com")

        elif platform.system() == "Windows":
            webbrowser.get('windows-default').open("https://google.com")

    elif  keyword == 'github':
        speak("opening github")

        if platform.system() == "Darwin":
            webbrowser.get('macosx').open("https://github.com")

        elif platform.system() == "Windows":
            webbrowser.get('windows-default').open("https://github.com")

    elif  keyword == 'teams':
        speak("opening teams")

        if platform.system() == "Darwin":
            os.system("open /Applications/Teams.app")

        elif platform.system() == "Windows":
            loc = os.path.join(os.environ['USERPROFILE'], "AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe")
            os.startfile(loc)

    elif keyword == 'spotify':
        speak("opening spotify")

        if platform.system() == "Darwin":
            os.system("open /Applications/Spotify.app")

        elif platform.system() == "Windows":
            loc = os.path.join(os.environ['APPDATA'], "Spotify\\Spotify.exe")
            os.startfile(loc)
            time.sleep(1)
            keyboard.press_and_release('Space')

    elif keyword == 'whatsapp':
        speak("opening whatsapp")

        if platform.system() == "Darwin":
            os.system("open /Applications/WhatsApp.app")

        elif platform.system() == "Windows":
            loc = os.path.join(os.environ['USERPROFILE'], "AppData\\Local\\WhatsApp\\WhatsApp.exe")
            os.startfile(loc)

    elif keyword == 'small_talk':
        
        context = f"You are a small talk module, just have fun with user by replying with a humorous answers [Query]: {query}"
        completion = completion_api_call(context)
        print(completion)
        speak(completion)

    elif keyword == 'close':

            print("Bye!!! it was nice meeting you.")
            speak("Bye!!! it was nice meeting you.")
            exit(0)