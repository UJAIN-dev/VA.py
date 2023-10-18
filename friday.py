import speech_recognition as sr
from action import speak, take_action
from chat_completetion import context_query

def main():
    print("\n\nHi My Name Is Friday")
    print("How can i be of your service")
    speak("Hi, My Name Is Friday")
    speak("How can i be of your service")

    while True:

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\n\nI am Listening...") 
            r.pause_threshold = 2
            audio = r.listen(source)

        try:
            print("Please wait I am Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n\n")
            take_action(context_query(query),query)

        except Exception as e:
            print(e)
            print("Say That Again Please...")

if __name__ == '__main__':
    main()