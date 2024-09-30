import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pywhatkit as kit
import os
import subprocess as sp


recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis.How may I help you Sir?")
    print("I am Jarvis.How may I help you Sir?")
    
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold==1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        command=r.recognize_google(audio,language='en-in')
        print(f"User said: {command}\n")
            
            
                
    except Exception as e:
        #print(e)
        print("Say that again please...")    
        return "None"
    return command

wishMe()



if __name__=="__main__":

   while True:

            command = takeCommand().lower()
            #print(command)
            if command==0:
                continue

            if 'hi' in command or 'hello' in command:
                speak("Hello sir, How may I help you?")
                
            if 'what are you' in command or 'tell me yourself' in command or 'introduce yourself' in command:
                speak(f"I'm JARVIS a virtual artificial intelligence. I'm here to assist you with a variety of tasks as best I can. ,JARVIS stands for Just A Rather Very Intelligent System ")
                
            elif 'how are you' in command:
                speak(f"I'm fine. What about u?")
                
            elif 'what are you doing' in command or 'are you there' in command:
                speak(f"I'm just waiting for your command,Sir!")
                
            elif 'i am good' in command or 'i am fine' in command:
                speak(f"That's great!! How may I help you sir?") 
                
            elif "good bye" in command or "ok bye" in command or "turn off" in command:
                speak ('Shutting down,Have a good day Sir!!!')
                break
            
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak('Current time is ' + time)
                print(time)    
                            
            elif 'date' in command:
                current_date = datetime.datetime.now().strftime("%m/%d/%y")
                speak(current_date)
                print(current_date)
                  
                    
            if 'wikipedia' in command:
                speak('What do you want to search on Wikipedia, sir?')
                search_query = takeCommand().lower()
                #statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(search_query, sentences=2)
                speak(f"According to Wikipedia, {results}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(results)

            elif 'open youtube' in command:
                speak('What do you want to search on Youtube, sir?')
                video = takeCommand().lower()
                kit.playonyt(video)
                speak("YouTube is open now")
                  
            elif 'open google' in command:
                speak('What do you want to search on google, sir?')
                google_search = takeCommand().lower()
                kit.search(google_search)
                speak("Google is open now")
                #time.sleep(5)

            elif 'open gmail' in command:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail is open now")
                #time.sleep(5)
                
            elif "send whatsapp message" in command:
                speak('On what number should I send the message sir? Please enter in the console: ')
                number = input("Enter the number: ")
                speak("What is the message sir?")
                message = takeCommand().lower()
                kit.sendwhatmsg_instantly(f"+91{number}", message)
                speak("I've sent the message sir.")
                
            elif 'play' in command:
                song = command.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)
            

            if 'open camera' in command:
                sp.run('start microsoft.windows.camera:', shell=True)
                speak("Camera is opened")

            elif 'open calculator' in command:
                sp.Popen( "C:\\Windows\\System32\\calc.exe")
                speak("Calculator is opened")
                
                
            if 'thank you' in command or 'well done' in command:
                speak(f"It's my pleasure Sir")
                
            elif 'idiot' in command or 'stupid' in command:
                speak(f"Sorry for my inconvenience sir...")
                
                
            elif 'genius' in command or 'smart' in command or 'great' in command:
                speak(f"Thank u sir")
                
            elif 'sorry' in command:
                speak(f"Never mind sir")



                