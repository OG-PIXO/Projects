import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")       


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query.lower()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        
        
        if query == "none":
            continue
        
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        
        elif 'play' in query:
            webbrowser.open("https://www.youtube.com/watch?v=kt14c7sYTFA")
        
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
elif 'set a timer for five minutes' in query:
        webbrowser.open("https://www.google.com/search?q=5+minute+timer%5D&rlz=1C1GCEA_enIN1040IN1040&oq=5+minute+timer%5D&aqs=chrome..69i57j0i10i512l2j0i512j0i10i512l5j46i10i512.6593j0j7&sourceid=chrome&ie=UTF-8")
     
