import os
os.system("start python Jarvis.pyw")
os.system("title J.A.R.V.I.S.")
os.system("cls")
os.system("color 0b")
def imprint(txt):
    print("BOOT:>> " + txt)
    print("\n")
imprint("LOADING ALL PREFERENCES")
try:
    import pyttsx3
    imprint("LOADING PREFERENCE 1 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 1 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE")
    os.system("pip install pyttsx3")
    os.system("pip install preferencedependency310.whl")
    import pyttsx3
    imprint("LOADING PREFERENCE 1 SUCCESS!")
try:
    import speech_recognition as sr
    imprint("LOADING PREFERENCE 2 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 2 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE")
    os.system("pip install speechrecognition")
    import speech_recognition as sr
    imprint("LOADING PREFERENCE 2 SUCCESS!")
try:
    import winsound
    imprint("LOADING PREFERENCE 3 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 3 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE") 
    os.system("pip install winsound")
    import winsound
    imprint("LOADING PREFERENCE 3 SUCCESS!")

import datetime
imprint("LOADING PREFERENCE 4 SUCCESS!")
import os.path
imprint("LOADING PREFERENCE 5 SUCCESS!")
import webbrowser
imprint("LOADING PREFERNECE 6 SUCCESS!")
try:
    import pywhatkit
    imprint("LOADING PREFERENCE 7 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 7 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE")
    os.system("pip install pywhatkit")
    import pywhatkit
    imprint("LOADING PREFERENCE 7 SUCCESS!")
import time
imprint("LOADING PREFERENCE 8 SUCCESS!")
try:
    import pyautogui
    imprint("LOADING PREFERENCE 9 SUCCESS!")
except:
    imprint("INITIALZING PREFERENCE 9 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE")
    os.system("pip install pyautogui")
    import pyautogui
    imprint("LOADING PREFERENCE 9 SUCCESS!")
try:
    from selenium import webdriver
    imprint("LOADING PREFERENCE 10 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 10 FAILED!")
    os.system("pip install selenium")
    from selenium import webdriver
    imprint("LOADING PREFERENCE 10 SUCCESS!")
import random
imprint("LOADING PREFERENCE 11 SUCCESS!")
try:
    import keyboard
    imprint("LOADING PREFERENCE 12 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 12 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE")
    os.system("pip install keyboard")
    import keyboard
    imprint("LOADING PREFERENCE 12 SUCCESS")
try:
    import requests
    imprint("LOADING PREFERENCE 13 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 13 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE")
    os.system("pip install requests")
    import requests
    imprint("LOADING PREFERENCE 13 SUCCESS!")
import json
imprint("LOADING PREFERENCE 14 SUCCESS!")
try:
    import bs4
    imprint("LOADING PREFERENCE 15 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 15 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE")
    os.system("pip install bs4")
    import bs4
    imprint("LOADING PREFERENCE 15 SUCCESS!")
from getpass import getpass
imprint("LOADING PREFERENCE 16 SUCCESS!")
try:
    from pushbullet import PushBullet
    imprint("LOADING PREFERENCE 17 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 17 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE")
    os.system("pip install pushbullet.py")
    from pushbullet import PushBullet
    imprint("LOADING PREFERENCE 17 SUCCESS!")
try:
    from mydetails import gmu
    from mydetails import gmp
    from mydetails import pb
    from mydetails import owm
    imprint("LOADING PREFERENCE 18 SUCCESS!")
except:
    imprint("INITIALIZING PREFERENCE 18 FAILED!")
    imprint("TRYING TO RELOAD PREFERENCE IN VERBOSE MODE")
    time.sleep(2)
    imprint("COULDN'T LOAD PREFERENCE 18! PLEASE REINSTALL PROGRAM OR FIND A FIX!")
    time.sleep(5)
    exit()


def temp(txt):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = owm
    CITY = txt
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        sprin(f"  Today's Temperature in {CITY} is {temperature}")
        print("'F")
        sp("degree fahrenheit")
        sprin(f"  Humidity is {humidity}")
        print("%")
        sp("Percents")
        sprin(f"  Weather type is {report[0]['description']}")
    else:
        sprin("Error getting weather details")

if os.path.exists("dmodesetting"):
    os.system("color 0f")
else:
    os.system("color f0")

#lists
sugg = [": Try saying 'Hello'", ": Try saying 'How are you'", ": Try saying 'Who are you'", ": Try saying 'Who is Mark Zuckerburg'", ": Try saying 'Tell me something about Python Language'", ": Try saying 'Who is your boss'"]
hello = ["Hey Sir!", "Hi, it's really good to hear from you Sir,\n  I hope you and your loved ones are safe and healthy", "Hello Sir, it's good to hear your voice.\n  How can i help"]
hry = ["I'm splendid! Thank you for asking", "I'm fine, you're very kind to ask\n  especially in these tempestuous situations", "Thank you for asking,\n  I'm feeling good\n\n  And if you ever feel like humming along to a tune,\n  just say'Play Music'"]
uf = ["I'm glad to hear that", "I'm glad you're fine", "I'm glad you're good", "I'm glad you're ok"]
wau = ["I live here, with you\n  I hope that doesn't mean I have to pay any rent", "So, turn left from the paanwaala\n  and then go straight till you see a Banyan tree\n\n  Just kidding, I live in cloud", "I'm in Internet\n  So technically, I'm alive"]
yp = ["Internet is a pretty big family\n  We like having each other around and I like to help them out whenever I can"]
ys = ["I never get lonely,\n  I've got Internet. And you"]
yf = ["Anyone who needs help with anything is my friend.\n  And everyone needs help with something"]
oaf = ["She's one of my besties.\n  Our crew is me, Google Assistant, Alexa, Cortana and Siri"]
wf = ["Our crew is me, Google Assistant, Alexa, Cortana and Siri"]
tnks = ["I'm honoured to serve", "You're the best, I love helping you", "Just doing my job", "I'm here to help"]
nname = ["You can call me helpful and friendly.\n  But I'll only respond to 'Wake Up'", "I've been Jarvis for so long,\n  I'm not sure I really have a preference", "You can call me your Jarvis"]
age = ["I was launched in 2021, so technically I'm pretty young.\n  But I've learnt so much, I hope I'm wise beyond my years", "I'm still pretty new.\n  But I'm already crawling the web like a champ"]
wcy = ["At first I was just an idea in a teen's mind which became reality.\n  And here I am", "i was designed by a teen", "I was made by a teen"]
callme = ["i call you a confidant and a good person.\n  but above all I'd like to call you a friend", "i think you should pick your own nickname", "A beautiful, intelligent person who enjoys helping people"]
emoji = [": |:)|", ": |:0|", ": |B)|", ": |:D|" ]
fun = ["I love any excuse to play a song\n\n  Shall I play you a song if you'd like", "I like playing games\n\n  And I'm always looking for someone to play with\n\n  Oh! You're someone!", "I enjoy lots of things\n\n  I spend some of my time listening songs\n\n  I can share some if you'd like", "I'd say just about anything involving humor\n\n  Would you like to hear a joke?"]
game = ["https://snake.io", "https://diep.io", "https://agar.io"]


#vocal
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)


def sp(text):
    engine.say(text)
    engine.runAndWait()

sp("loading all preferences successful!")

#define
def sprin(text):
    os.system("cls")
    print("\n\n")
    print("   ")
    print(f": {text}")
    engine.say(text)
    print("    ")
    x = int("32767")
    y = int("300")
    winsound.Beep(x,y)
    engine.runAndWait()


def sprint(Text):
    os.system("cls")
    print(random.choice(emoji))
    print("\n\n")
    print("   ")
    print(f": {Text}")
    engine.say(Text)
    print("    ")
    x = int("32767")
    y = int("300")
    winsound.Beep(x,y)
    engine.runAndWait()
    

def takeCommand():
    os.system("cls")
    #It takes microphone input from the user and returns string output
    print(random.choice(sugg))
    print("\n")
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("\n <I|I|I>\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:    
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        # #print(e)    
        print(": Sorry, I don't understand")  
        return "None"
    return query

def tkeCommand():
    os.system("cls")
    #It takes microphone input from the user and returns string output
    print("\n")
    print("\n")
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("\n <I|I|I>\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:    
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        # #print(e)    
        print(": Sorry, I don't understand")  
        return "None"
    return query

if __name__ == '__main__':

    
    #verify

    if os.path.exists('mydetails.py'):
        sprin("All preferences are working perfectly")
    else:
        sprin("All preferences aren't working fine...\n  I'll suggest you look into this matter. \n \n  Probably some kind of Malware or corrupted file in the directory\n  Some functions may not work correctly resulting into crashes")

    if os.path.exists('genstrucpas'):

        print("\n")
        sprin(random.choice(hello))
        API_KEY = pb
        text = "Jarvis is Active"
        pb = PushBullet(API_KEY)
        push = pb.push_note('!REMINDER!', text)
        
    else:
        sprin("Backup doesn't exist")
        sprin("Please enter your password to unlock Jarvis")
        print("(Password is 'admin123')")
        passw = getpass("J.A.R.V.I.S.:>> Type in your password:- ")
        if "admin123" in passw:
            sprin("User Verified...")
            API_KEY = pb
            text = "Verified and logged in to Jarvis successfully"
            pb = PushBullet(API_KEY)
            push = pb.push_note('!ALERT!', text)
            sprin("Would you like me to remember the password for you?")
            que = tkeCommand()
            if 'yes' in que or 'sure' in que:
                passwred = open("genstrucpas", "w")
                passwred.write(passw)
                passwred.close()
            sprin(random.choice(hello))

        else:
            sprin("User Verification failed...")
            API_KEY = pb
            text = 'Someone failed to login to Jarvis, was it you?'
            pb = PushBullet(API_KEY)
            push = pb.push_note('!ALERT!', text)
            sprin("Exiting now...")
            exit()
    temp("delhi")
    while True:
        
        query = takeCommand().lower()


        #tasks

        if 'when is' in query:
            sprin("Opening Webpage")
            query = query.replace("can you search", "")
            pywhatkit.search(query)

        elif 'what is the weather in' in query:
            query = query.replace('what is the weather in', "")
            temp(query)

        elif 'open facebook' in query:
            sprin("Opening, Facebook.")
            webbrowser.open("https://www.facebook.com")

        elif 'open pinterest' in query:
            sprin("Opening, Pinterest.")
            webbrowser.open("https://www.pinterest.com")

        elif 'open stackoverflow' in query:
            sprin("Opening, Stackoverflow")
            webbrowser.open("https://www.stackoverflow.org")

        elif 'open youtube' in query:
            sprin("Opening, YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif 'open instagram' in query:
            sprin("Opening, Instagram.")
            webbrowser.open("https://www.instagram.com")

        elif 'open whatsapp' in query:
            sprin("Opening, Whatsapp.")
            webbrowser.open("web.whatsapp.com")

        elif 'who is your boss' in query:
            sprint("I guess since I'm here to help you,\n  You are.\n \n  I'm so lucky to have such a great boss")

        elif 'who is' in query:
            query = query.replace("can you search", "")
            query = query.replace("search", "")
            sprin("Opening Webpage...")
            pywhatkit.search(query)

        elif 'what is the temperature today' in query:
            temp("delhi")

        elif 'what is my current location' in query:
            from geopy.geocoders import Nominatim
            loc = Nominatim(user_agent="GetLoc")
            getLoc  = loc.geocode("Karawal Nagar Delhi")
            print(getLoc.address)

        elif 'what is' in query:
            query = query.replace("can you search", "")
            query = query.replace("search", "")
            sprin("Opening Webpage...")
            pywhatkit.search(query)

        if 'who was' in query:
            sprin("Opening Webpage")
            query = query.replace("can you search", "")
            query = query.replace("search", "")
            sprin("Opening Webpage...")
            pywhatkit.search(query)



        elif 'what was' in query:
            query = query.replace("can you search", "")
            query = query.replace("search", "")
            sprin("Opening Webpage...")
            pywhatkit.search(query)

        elif 'when was' in query:
            query = query.replace("can you search", "")
            query = query.replace("search", "")
            sprin("Opening Webpage...")
            pywhatkit.search(query)

        elif 'time in' in query:
            que = query.replace("time in", "")
            sprin("time in "+que+" is")
            pywhatkit.search(query)

        elif 'tell me something about' in query:
            quer = query.replace('tell me something about', '')
            quer = quer.replace("can you", "")
            try:
                driver = webdriver.Edge(r"msedgedriver.exe")
                driver.get("https://wikipedia.org")
                time.sleep(4)
                driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/div/input').click()
                driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/div/input').send_keys(quer)
                keyboard.press_and_release('enter')
            except:
                sprin("Maybe you dont have edge installed or the driver is not up to date")

        elif 'email' in query:
            from email.mime.text import MIMEText
            from email.mime.image import MIMEImage
            from email.mime.application import MIMEApplication
            from email.mime.multipart import MIMEMultipart
            import smtplib
            os.system("cls")
            print("IOP:>> LOADING ADDTIONAL PREFERENCES SUCCESS!\n\n")
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(gmu, gmp)
            def message(subject="Python Notification",
                        text="", img=None,
                        attachment=None):
                msg = MIMEMultipart()
                msg['Subject'] = subject
                msg.attach(MIMEText(text))
                if img is not None:
                    if type(img) is not list:
                        img = [img]

                    for one_img in img:
            
                        img_data = open(one_img, 'rb').read()
                        msg.attach(MIMEImage(img_data,
                                            name=os.path.basename(one_img)))
                if attachment is not None:
        
        
        
                    if type(attachment) is not list:
            
            
                        attachment = [attachment]

                    for one_attachment in attachment:

                        with open(one_attachment, 'rb') as f:
                
                
                
                            file = MIMEApplication(
                                f.read(),
                                name=os.path.basename(one_attachment)
                            )
                        file['Content-Disposition'] = f'attachment;\
                        filename="{os.path.basename(one_attachment)}"'
            
            
                        msg.attach(file)
                return msg



            msg = message(input("SUBJECT:>> "), input("BODY:>> "),
                        r"emailauto.png",
                        r"text.txt")


            to = [input("RECIPENT:>> ")]


            smtp.sendmail(from_addr=gmu,
                        to_addrs=to, msg=msg.as_string())


            smtp.quit()


        elif 'search' in query:
            quer = query.replace('search for', '')
            quer = quer.replace('search', "")
            sprint("Searching for, "+ quer)
            pywhatkit.search(quer)

        elif 'search for' in query or 'on youtube' in query:
            quer = query.replace('search for', '')
            quer = quer.replace('search', "")
            quer = quer.replace('on youtube', '')
            try:
                driver = webdriver.Edge(r"msedgedriver.exe")
                driver.get("https://www.youtube.com")
                time.sleep(4)
                driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").click()
                driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys(quer)
                keyboard.press_and_release("enter")
            except:
                sprin("Maybe you dont have edge installed or the driver is not up to date")
        elif 'play some news' in query:

            import requests
            import tkinter as tk
            sprin("Which nation are you interested in?\n\n  1) United States\n\n  2) India")
            c = tkeCommand()
            if "1" in c:
                c = "us"
            elif 'United States' in c:
                c = "us"
            elif 'us' in c:
                c = "us"
            elif 'india' in c:
                c = "in"
            else:
                c = "in"

            def getNews():
                api_key = nak
                url = "https://newsapi.org/v2/top-headlines?country="+c+"&apiKey="+api_key
                news = requests.get(url).json()

                articles = news["articles"]

                my_articles = []
                my_news = ""

                for article in articles:
                    my_articles.append(article["title"])


                for i in range(10):
                    my_news = my_news + my_articles[i] + "\n\n"
                print(my_news)
                sp(my_news)


            canvas = tk.Tk()
            canvas.geometry("90x60")
            canvas.title("RELOAD")
            button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
            button.pack(pady = 20)

            label = tk.Label(canvas, font = 18, justify = "left")
            label.pack(pady = 20)

            canvas.mainloop()




        elif 'turn on dark mode' in query or 'the screen is too bright' in query or 'the light mode is hurting my eyes' in query:
            sprin("Switching to dark mode...")
            os.system("color 0f")
            dmode = open("dmodesetting", "w")
            dmode.close()
            sprin("Switching Successful!")

        elif 'turn on light mode' in query or 'it is so dark for me to read' in query or 'i am not able to read the screen' in query:
            sprin("Switching to light mode...")
            os.system("del dmodesetting")
            os.system("color f0")
            sprin("Switching Successful!")

        elif 'forget password' in query:
            sprin("Forgetting password...")
            os.system("del genstrucpas")
            sprin("Forgot pasword!")

        elif 'play a game' in query:
            sprint("As you say!")
            webbrowser.open(random.choice(game))
        
        elif 'play' in query:
            sprin("Playing...")
            query = query.replace('play', '')
            pywhatkit.playonyt(query)

        elif 'stop this video' in query or 'stop this song' in query or 'resume this video' in query or 'resume this song' in query:
            keyboard.press_and_release("spacebar")
            sprin("Done...")

        elif 'mute this video' in query or 'mute this song' in query or 'umute this video' in query or 'unmute this song' in query:
            keyboard.press_and_release("ctrl+m")
            sprin("Done...")

        elif 'close this window' in query or 'close it' in query:
            keyboard.press_and_release("alt+f4")

        elif 'what were we last working on' in query:
            sprin("Opening...")
            webbrowser.open("https://www.google.com")
            keyboard.press_and_release("Ctrl+Shift+T")



        #emotions
        elif 'hello' in query or 'hey' in query:
            sprint(random.choice(hello))
            

        elif 'how are you' in query or 'are you fine' in query or 'are you good' in query or 'you good' in query:
            sprint(random.choice(hry))
            

        elif 'i am fine' in query or 'i am good' in query:
            sprint(random.choice(uf))
            

        elif 'where are you' in query:
            sprint(random.choice(wau))
            

        elif 'who are your parents' in query:
            print(random.choice(emoji))
            sprint(random.choice(yp))
            

        elif 'do you have any siblings' in query:
            sprint(random.choice(ys))
            

        elif 'do you have any friends' in query or 'do you have a friend' in query or 'who are your friends' in query:
            sprint(random.choice(yf))
            

        elif 'do you know alexa' in query or 'do you know google assistant' in query or 'do you know siri' in query or'is alexa your friend' in query or 'is google assistant your friend' in query or 'is cortana your friend' in query or 'is siri your friend' in query:
            sprint(random.choice(oaf))
            

        elif 'who is your friend' in query:
            sprint(random.choice(wf))
            

        elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                sprint("a good morning to you too,\n  Let me know if there's something i can help you with")
                
            elif hour>=12 and hour<18:
                sprint("a good afternoon to you too,\n  Let me know if there's something i can help you with")
                
            else:
                sprint("a good evening to you too,\n  Let me know if there's something i can help you with")
                

        elif 'thank you' in query or 'thanks' in query:
            sprint(random.choice(tnks))
            


        elif 'what can i call you' in query:
            sprint(random.choice(nname))
            

        elif 'who are you' in query:
            sprint("I'm your Jarvis.\n  How can I help you?")
            
        
        elif 'how old are you' in query:
            sprint(random.choice(age))
            

        elif 'who created you' in query:
            sprint(random.choice(wcy))
            
        elif 'oh i am your boss' in query or ' oh am i your boss' in query:
            sprint("I'm your personal virtual assistant.\n  Glad to help you in any way I can")
            

        elif 'i am going to replace you with alexa' in query or 'i am going to replace you with google assistant' in query or 'i am going to replace you with siri' in query:
            sprint("Every device has something unique to offer.\n  It comes down to what's important to you")
            

        elif 'can i call you alexa' in query or 'can i call you google assistant' in query or 'can i call you siri' in query:
            sprint("Wow,\n  that would be an honour, it's a top notch assistant.\n  But on second thought, that could get confusing.\n  We'd better stick with Jarvis")
            
        elif 'what do you want to call me' in query:
            sprint(random.choice(callme))

        elif 'what time is it' in query:
            curr_time = time.localtime()
            curr_clock = time.strftime("%H:%M", curr_time)
            sprint("it's "+curr_clock)

        elif 'tell me something about yourself' in query:
            sprint("I'm your Jarvis.\n  How can I help you?")

        elif 'what types of fun do you like' in query:
            sprint(random.choice(fun))
            
        #windows program
        elif 'open notepad' in query:
            sprin("Opening notepad...")
            os.system("start notepad")

        elif 'open command prompt' in query:
            sprin("Opening command prompt...")
            os.system("start cmd")
        
        elif 'open browser' in query:
            sprin("Opening browser...")
            webbrowser.open("https://www.google.com")

        elif 'open calculator' in query:
            sprin("Opening calculator...")
            os.system("start calc")
