import pyttsx3  # text to speech
import datetime
import speech_recognition as sr # string output from microphone input
import wikipedia
import webbrowser # opens the prompted website
import os.path
import smtplib # work with queries related to email

engine = pyttsx3.init('sapi5') # Microsoft speech api
voices = engine.getProperty('voices') #gets you the details of the current voice
engine.setProperty('voice',voices[1].id) #0-male voice

def speak(audio):   
    engine.say(audio)    
    engine.runAndWait() #Without this command, speech will not be audible to us.


def wishme():
    hour = int(datetime.datetime.now().hour)
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")    
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")       
    
    else:
        speak("Good Evening!")

if __name__ == "__main__":
    speak("Hey")
    wishme()
    speak('Yash , I am Jarvis your AI assistant. Please tell me how may I help you')
    