import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes
import webbrowser
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer,QTime,QDate
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from interface import Ui_Form

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices') # getting voice for our Jarvis
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)             # speaking function
    engine.runAndWait()
    
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.TaskExecution()
    
    def wishings(self):
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("Good Morning Master")
            speak("Good Morning Master")
        elif hour>=12 and hour<17:
            print("Good Afternoon Master")
            speak("Good Afternoon Master")
        elif hour>=17 and hour<21:
            print("Good Evening Master")
            speak("Good Evening Master")
        else:
            print("Good Night Master")
            speak("Good Night Master")
        
    def commands(self): 
        r=sr.Recognizer()
        with sr.Microphone() as source:     # catch the audio on microphone and store
            print("Listening...")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)
            
        try:         # sending audio to google and convert into text
            print("Wait for few moments....")
            query=r.recognize_google(audio,language='en-in')
            print(f"You just said : {query}\n")
        except Exception as e:
            print(e)
            speak("please tell me again")
            query="none"
            
        return query
    
    def wakeUpCommands(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Jarvis is Sleeping...")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)
            
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f"User Said:{query}\n")
            
        except Exception as e:
            print(e)
            query="none"
        return query
    
    def TaskExecution(self):
        while True:
            self.query=self.wakeUpCommands().lower()
            if "wake up" in self.query or "get up" in self.query or "listen" in self.query:
                print("....")
                self.wishings()
                speak("Yes Master What can I do for you !")
                while True:
                    self.query=self.commands().lower()
    
                    if 'time' in self.query:
                        strTime=datetime.datetime.now().strftime("%H:%M:%S")
                        speak("Sir, the time is : "+strTime)
                        print(strTime)
    
                    elif 'open browser' in self.query:
                        speak('Opening Browser Master')
                        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                        while True:
                            chromeQuery=self.commands().lower()
                            if "search" in chromeQuery:
                                youtubeQuery=chromeQuery
                                youtubeQuery=youtubeQuery.replace("search","")
                                pyautogui.write(youtubeQuery)
                                pyautogui.press('enter')
                                speak('Searching...')
                            
                            elif "close browser" in chromeQuery or "exit browser" in chromeQuery or "close window" in chromeQuery or "close this window" in chromeQuery:
                                pyautogui.hotkey('ctrl','w')
                                speak("Closing Browser Master...")
                                break
            
                    elif 'wikipedia' in self.query:
                        speak('Searching in wikipedia')
                        try:
                            self.query=self.query.replace('wikipedia','')
                            results=wikipedia.summary(self.query,sentences=1)
                            speak("According to Wikipedia..")
                            print(results)
                            speak(results)
                        except:
                            print("No results found..")
                            speak("no results found")
                            
                    elif  'open youtube' in self.query:
                        print("Opening Youtube")
                        speak("Opening Youtube")
                        webbrowser.open("youtube.com")
                            
                    elif 'play' in self.query:
                        playQuery=query.replace('play','')
                        speak("Playing "+playQuery)
                        pywhatkit.playonyt(playQuery)  #playing video on youtube
                
                    elif "open notepad" in self.query:
                        speak("Opening Notepad Application Master...")
                        os.startfile('C:\\Windows\\system32\\notepad.exe')
                        while True:
                            notepadQuery=self.commands().lower()
                            
                            if "paste" in notepadQuery:
                                pyautogui.hotkey('ctrl','v')
                                speak("Done Master!")
                                
                            elif "save this file" in notepadQuery:
                                pyautogui.hotkey('ctrl','s')
                                speak("Master, Please specify a name for this file")
                                notepadSavingQuery=commands()
                                pyautogui.write(notepadSavingQuery)
                                pyautogui.press('enter')
                                
                            elif "type" in notepadQuery:
                                speak("Please tell me what should i write...")
                                while True:
                                    writeInNotepad=commands()
                                    if writeInNotepad=='exit typing':
                                        speak("Done Master.")
                                        break
                                    else:
                                        pyautogui.write(writeInNotepad)
                                        
                            elif "exit notepad" in notepadQuery or "close notepad" in notepadQuery:
                                speak("Quiting Notepad Master...")
                                pyautogui.hotkey('ctrl','w')
                                break
                                
                    elif 'minimize' in self.query or 'minimise' in self.query:
                        #pyautogui.moveTo(1232,15)
                        #pyautogui.leftClick()
                        speak("Minimizing Master")
                        pyautogui.hotkey('win','down','down')
                  
                    elif 'joke' in self.query:
                        Joke=pyjokes.get_joke()
                        print(Joke)
                        speak(Joke)
                        
                    elif "mute" in self.query or "sleep" in self.query:
                        speak("I'm Muting Master...")
                        break
                    
                    elif 'exit program' in self.query or  'exit the program' in self.query:
                        speak("I'm Leaving Master, Byee...")
                        sys.exit()
                        
                    elif "magic sentence" in self.query:
                        speak("Yes Master,for your pleasure !!!")
                        
                    elif "what can you do for me" in self.query:
                        speak("Yes Master,Nice Question")
                        speak("As per my Program,I'm a bot which can perform tasks through your voice commands")
                        
                    elif "cool" in self.query or "nice" in self.query or "awsome" in self.query or "thank you" in self.query:
                        speak("Yes Master, That's my Pleasure!")
                        
                    elif "maximize" in self.query or "maximise" in self.query:
                        speak("Maximizing Master")
                        pyautogui.hotkey('win','up','up')
                        
                    elif "close the window" in self.query or 'close the application' in self.query:
                        speak("Closing Master")
                        pyautogui.hotkey('ctrl','w')
                        
                    elif "screenshot" in self.query:
                        speak("Taking Screenshot Master...")
                        pyautogui.hotkey('win','printscreen')
                        speak("Screenshot taken")
                        
                    elif "open paint" in self.query:
                        speak("Opening Paint Application Master....")
                        os.startfile("C:\\Windows\\system32\\mspaint.exe")
                        while True:
                            paintQuery=self.commands().lower()
                            if "close" in paintQuery:
                                speak("Closing the Application Master")
                                pyautogui.leftClick(x=1344,y=11)
                                break
                            
                            elif "paste" in paintQuery:
                                pyautogui.hotkey('ctrl','v')
                                speak("Done Master!")
                                
                            elif "save" in paintQuery:
                                pyautogui.hotkey('ctrl', 's')
                                speak("Done Master!")
                                
                            elif "minimize" in paintQuery or "minimise" in paintQuery:
                                speak("Minimizing Master")
                                pyautogui.hotkey('win','down','down')
                                
                            elif "maximize" in paintQuery or "maximise" in paintQuery:
                                speak("Maximizing Master")
                                pyautogui.hotkey('win','up','up')
                            
startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.startpushButton.clicked.connect(self.startTask)
        self.ui.quitpushButton.clicked.connect(self.close)
        
    def startTask(self):
        # Voice
        self.ui.movie=QtGui.QMovie("C:\\Users\\ASHOK\\Documents\\ASHOK\\Projects\\AI [Desktop Voice Assistant]\\Model-2\\GUI\\Aqua.gif")
        self.ui.voice.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        #Iron
        self.ui.movie=QtGui.QMovie("C:\\Users\\ASHOK\\Documents\\ASHOK\\Projects\\AI [Desktop Voice Assistant]\\Model-2\\GUI\\iron.jpg")
        self.ui.iron.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        #date
        self.ui.movie=QtGui.QMovie("C:\\Users\\ASHOK\\Documents\\ASHOK\\Projects\\AI [Desktop Voice Assistant]\\Model-2\\GUI\\td.jpg")
        self.ui.date.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        #time
        self.ui.movie=QtGui.QMovie("C:\\Users\\ASHOK\\Documents\\ASHOK\\Projects\\AI [Desktop Voice Assistant]\\Model-2\\GUI\\td.jpg")
        self.ui.time.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        #earth
        self.ui.movie=QtGui.QMovie("C:\\Users\\ASHOK\\Documents\\ASHOK\\Projects\\AI [Desktop Voice Assistant]\\Model-2\\GUI\\Earth.gif")
        self.ui.earth.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        #start
        self.ui.movie=QtGui.QMovie("C:\\Users\\ASHOK\\Documents\\ASHOK\\Projects\\AI [Desktop Voice Assistant]\\Model-2\\GUI\\Start.png")
        self.ui.start.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        #quit
        self.ui.movie=QtGui.QMovie("C:\\Users\\ASHOK\\Documents\\ASHOK\\Projects\\AI [Desktop Voice Assistant]\\Model-2\\GUI\\Quit.png")
        self.ui.quit.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
    def showTime(self):
        currentTime=QTime.currentTime()
        currentDate=QDate.currentDate()
        labelTime=currentTime.toString('hh:mm:ss')
        labelDate=currentDate.toString(Qt.ISODate)
        self.ui.datetextBrowser.setText(f"Date: {labelDate}")
        self.ui.timetextBrowser.setText(f"Time: {labelTime}")
        
app=QApplication(sys.argv)
jarvis=Main()
#ui=UI_Form()
jarvis.show()
sys.exit(app.exec_())