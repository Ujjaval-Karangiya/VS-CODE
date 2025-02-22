import speech_recognition as sr
import webbrowser
import pyttsx3
import mysong
from openai import OpenAI 
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def pc(c):
    if (c.lower() == "open google"):
        webbrowser.open("https://www.google.com/")
    elif (c.lower() == "open youtube"):
        webbrowser.open("https://www.youtube.com/")
    elif (c.lower() == "open instagram"):
        webbrowser.open("https://www.nstagram.com/")
    elif (c.lower() == "open facebook"):
        webbrowser.open("https://www.nstagram.com/")  
    elif (c.lower() == "open mia khalifa"):
        webbrowser.open("https://okxxx2.com/sites/mia-khalifa/")  
    elif (c.lower() == "open ok"):
        webbrowser.open("https://www.ok.xxx/")
    elif (c.lower() == "open master"):
        webbrowser.open("https://xhaccess.com/search/xhmaster+sex+video+xhamaster+sex+xhmaster+sex?quality=720p")   
    elif (c.lower().startswith("play")):
        msong = c.lower().split(" ")[1]
        music=mysong.song[msong]
        webbrowser.open(music)
    else:
        print("somthing: known")
             
if __name__=="__main__":
    speak("initialization of ai.......")
    while True:
        r = sr.Recognizer()
        speak("now you can call ai")
        try:
            with sr.Microphone() as source:
                print("listening........")
                audio = r.listen(source)
            word =r.recognize_google(audio)
            # word =input("what is key : ")
            if (word.lower() == "java"):
                speak("speak brother how can i help you")
                with sr.Microphone() as source:
                     print("bol ne lodeee")
                     audio = r.listen(source)
                     command =r.recognize_google(audio)
                    #  command =input("what you want :")      
                     pc(command)
        except Exception as e:
            print("error; {0}".format(e))
            break


    
    
    
    