#modules
import speech_recognition as sr  #capture and recognizes the speech
import pyttsx3  #text-to-speech
from datetime import datetime  #fetch date and time
import requests
import webbrowser  #web searches

#Initialize the recognizer and text-to-speech engine

recognizer = sr.Recognizer()
engine = pyttsx3.init()

#voice control
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#greeting
def get_greeting():
    current_hour = datetime.now().hour
    if 0 <= current_hour <12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"
    
#functions
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""

def tell_time():
    now = datetime.now()
    return now.strftime("%H:%M")

def tell_date():
    today = datetime.today()
    return today.strftime("%B %d, %Y")

def search_web(query):
    url = f"https://www.google.com/search?={query}"
    webbrowser.open(url)
    return f"Here are the results for {query}"

#main function

def main():
    greeting = get_greeting()
    speak(f"{greeting}, How can I help you today?")

    while True:
        command = listen()
        
            #commands
        if "hello" in command:
            speak(f"{greeting}")
        elif "what's the time" in command:
            current_time = tell_time()
            speak(f"The current time is {current_time}")
        elif "today's date" in command:
            current_date = tell_date()
            speak(f"Today's date is {current_date}")
        elif "open" in command:
            website = command.replace("open", "").strip()
            url = f"https://{website.lower()}.com"
            speak(f"opening {website}...")
            webbrowser.open(url)
        elif "stop" in command or "exit" in command:
            speak("GoodBye")
            break
        else:
            speak("Sorry, I didnt know that command.Please try again.")

if __name__ == "__main__":
    main()
            
            
    
    



