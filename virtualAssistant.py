import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import keyboard
import random
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
        
    else:
        speak("Good Evening !")  
        
    speak("I am Sophia.. Sir ")     
    
def getName():
    global uname
    speak("Can I please know your name?")
    uname = takeCommand()
    print("Name:",uname)
    speak("I am glad to know you")
    speak(uname) 
    speak("Hope you're doing good. Please tell me how may I help you")     
            
def takeCommand():
    '''it takes microphone input from the user and returns the string output'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)        
        
    try:
        print("Recognizimg...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")      
    
    except Exception as e:
        #  print(e)
        print("Say that again please...")        
        return "None"
    return query

def sendEmail(to, content):
    print("Sending mail to ", to)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #paste your email id and password in the respective places
    server.login('your email id', 'password') 
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == "__main__":
        wishMe()
        getName()
        while True:
           query = takeCommand().lower()
           # logic for executing tasks based on query
           
           if "open" in query:
               query = query.replace("open","")
               query = query.replace("sophia","")
               pyautogui.FAILSAFE = False
               pyautogui.press("super")
               pyautogui.typewrite(query)
               pyautogui.sleep(1)
               pyautogui.press("enter")

           elif "google" in query:
               from searchnow import searchGoogle
               searchGoogle(query)
               
           elif "youtube" in query:
               from searchnow import searchYoutube
               searchYoutube(query)
               
           elif "wikipedia" in query:
               from searchnow import searchWikipedia
               searchWikipedia(query)
            
           elif "pause" in query:
               pyautogui.press("k")
               speak("video paused")
               
           elif "replay the video" in query:
               pyautogui.press("k")
               speak("video played")
               
           elif "volume up" in query:
               from keyboard import volumeup
               speak("turning volume up, Sir")
               
           elif "volume down" in query:
               from keyboard import volumedown
               speak("turning volume down, Sir")       
    
           elif "play music" in query:  
               music_dir = "C:\\Users\\joshi\\Music"
               songs = os.listdir(music_dir)
               s = random.randint(0,9)
               os.startfile(os.path.join(music_dir,songs[s]))
               
           elif "the time" in query:
               strtime = datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"Sir, the time is {strtime}")
               
           elif "the date today" in query:
               date = datetime.datetime.now().strftime("%B %d, %Y")
               speak(f"Sir, the date is {date}")
               
           elif "send mail" in query:
               try:
                   speak("Whom should I send the mail")

                   to = input()
                   speak("What is the body?")
                   content = takeCommand()
                   sendEmail(to, content)
                   speak("Email has been sent successfully !")
                 
               except Exception as e:
                  print(e)
                  speak("I am sorry, not able to send this email")

           elif "activate how to do" in query:
               from pywikihow import search_wikihow
               speak("Activated, Please tell me what you want to know")
               how = takeCommand()
               try:
                   if "exit" in how or "close" in how:
                       speak("okay sir, how to do mode is closed")
                       break
                   else:
                       max_results = 1
                       how_to = search_wikihow(how, max_results)
                       assert len(how_to) == 1
                       how_to[0].print()
                       speak(how_to[0].summary)
               except Exception as e:
                   speak("sorry sir, I am not able to find this")
                   
           elif "how much battery we have" in query:
               import psutil
               battery = psutil.sensors_battery()
               percentage = battery.percent
               speak(f"sir our system have {percentage} percent battery")
               
           elif "play a game" in query:
               ppath = "C:\\Users\\vansh\\Desktop\\fav\\Assasin Run"
               os.startfile(ppath)
               
           elif "temperature" in query:
               search = "temperature in "
               url = f"https://www.google.com/search?q={search}"+ query
               r = requests.get(url)
               data = BeautifulSoup(r.text,"html.parser")
               temp = data.find("div",class_ = "BNeawe").text
               speak(f"current {search} is {temp}")
               
           elif "exit" in query:
              speak("Thanks for giving me your time, and have a nice day !")
              exit()