import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import requests
from pprint import pprint

f='C:/Program Files (x86)/Mozilla Firefox/firefox.exe'
webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(f))


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir! I'm Jarvis. How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	return res.json();

def speak_weather(result,city):
	speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	speak("Wind speed: {} m/s".format(result['wind']['speed']))
	speak("Description: {}".format(result['weather'][0]['description']))
	speak("Weather: {}".format(result['weather'][0]['main']))

def mainspeak():
	city=takeCommand().lower()
	print()
	try:
	  query='q='+city;
	  w_data=weather_data(query);
	  speak_weather(w_data, city)
	  print()
	except:
	  print('City name not found...')
        
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        
        #Logic for Task
        if 'search wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("search wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.get('firefox').open("youtube.com")
        elif 'open google' in query:
            speak("opening google...")
            webbrowser.get('firefox').open("google.com")
        elif 'open niit' in query:
            speak("opening moodle...")
            webbrowser.get('firefox').open("https://moodle.niituniversity.in/")
        elif 'open erp' in query:
            speak("opening nucleus...")
            webbrowser.get('firefox').open("https://nucleus.niituniversity.in/")
        elif 'open facebook' in query:
            speak("opening facebook...")
            webbrowser.get('firefox').open("https://www.facebook.com/")
        elif 'play music' in query:
            music_dir='E:\\Songs'
            songs=os.listdir(music_dir)
            x=random.randint(0,len(songs)-1)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[x]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            speak("opening visual studio code...")
            codepath='"C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"'
            os.startfile(codepath)
        elif 'open snake' in query:
            speak("opening snake xenzia...")
            codepath="C:\\Users\\dell\\Documents\\Snake Xenzia v1.0\\dist\\Snake.exe"
            os.startfile(codepath)
        elif 'open calculator' in query:
            speak("opening calculator...")
            codepath="C:\\Users\\dell\\Documents\\Scientific Calculator v1.0\\dist\\SCGUI.exe"
            os.startfile(codepath)
        elif 'your name' in query:
            speak("Jarvis sir!")
        elif 'hi jarvis' in query:
            speak("hello sir!")
        elif 'open study' in query:
            speak('opening study material...')
            os.startfile("F:\\NIIT University")
        elif 'my name' in query:
            speak("Anurag Porel")
        elif 'thank you' in query:
            speak("you are most welcome sir!")
        elif 'good job' in query:
            speak("thank you sir!")
        elif 'nice jarvis' in query:
            speak("thank you sir!")
        elif 'weather today' in query:
            speak('your location sir?')
            mainspeak() 
        elif 'send email' in query:
            try:
                speak("what should I say?")
                content=takeCommand()
                to="receiveremail@gmail.com"
                sendEmail(to, content)
                speak("email has been sent sir!")
            except Exception as e:
                #print(e)
                speak("Sorry sir! Unable to send the mail")
        elif 'stop jarvis' in query:
            speak("activating shut down protocol...")
            break

