import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your api key "
# you can get this on https://newsapi.org this website
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    global reading_news
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    
        
    elif c.lower().startswith("play"):
        song = c.lower().split("play")[1].strip()
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find the song in your library.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
        articles = data.get('articles', [])

        for article in articles:
            speak(article['title'])
            if not reading_news:
                break
        speak(article['title'])
    elif "stop" in c.lower():
        reading_news = False

        

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    print("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)

                if word.lower() == "jarvis":
                    speak("Welcome sir, what can I do for you?")
                    print("Welcome sir, what can I do for you?")

                    with sr.Microphone() as source:
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)
        except sr.UnknownValueError:
            print("I can't understand that.")
        except sr.RequestError as e:
            print(f"Could not request result; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
# so this is a basic jarvis that opens youthube facebook and google and github

