import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
 
 

engine= pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    speak("Hello there i am your personal assistant David nice to meet you")
    hour = int(datetime.datetime.now().hour)
    if hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("how may I help you?")
    


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        speech = r.listen(source,timeout=5, phrase_time_limit=3)
    try:
        print("Recognising")
        query = r.recognize_google(speech,language='en-in')
        print("user said:"+query)
    except Exception as e:
        print("Please say that again")
        return "None"
    return query

if __name__ == "__main__":
    
    
    while True:
        command = takecommand().lower()
        if 'wikipedia' in command:
           print("searching wikipedia...")
           command= command.replace('wikipedia', '')
           results = wikipedia.summary(command, sentences=2)
           speak("According to wikipedia")
           speak(results)
           print(results)
        
        elif "time" in command:
            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            sec = int(datetime.datetime.now().second)
            speak("The time is") 
            speak(hour) 
            speak(min) 
            speak(sec)
            
        elif "music" in command:
            webbrowser.open("https://www.youtube.com/watch?v=OPf0YbXqDm0&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj")
            speak("hope you like POP")
        elif "youtube" in command:
            print("searching youtube...")
            command= command.replace('youtube', '')
            url = "https://www.youtube.com/results?search_query=" + command
            webbrowser.open(url)
        
        elif "goodbye" in command:
            speak("have a nice day")
            exit()
        
        elif "what" and "is" in command:
            print("searching in goolge...")
            command= command.replace('what' and 'is', '')
            results= wikipedia.summary(command, sentences = 3)
            print(results)            
            speak(results)


        elif "hello" in command:
            wishme()
        elif "yourself" in command:
            version1= "Hello there i am David, your personal assistant."
            speak(version1)
            version2="i am created using python 3.8 and a few of the the python modules that inculde modules like pyttsx3 for my voice, speech recognition for being able to recognise your voice etcetra"
            speak(version2)
            version3=" i can do many things that include opening browser, playing music, search for different terms on google, wikipedia and youtube"
            speak(version3)
            version4=" but rember to use all the necessary keywords while searching for a query"
            speak(version4)
            example= " when you need to search for a video on youtube just tell me the name of the video and use the keyword after it, in this case that will be youtube. and the same goes for all the other keywords"
            speak(example)
        elif "open browser" in command:
            webbrowser.open("https://google.com")
        elif "who made you" in command:
            speak("i am made by The One and Only one wink wink")
            speak("hopes that helps")
