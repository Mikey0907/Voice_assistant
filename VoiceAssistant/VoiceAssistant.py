from __future__ import print_function
import os.path
import subprocess
import time
import warnings
import ctypes
import winshell
import pyjokes
import wikipedia
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import smtplib
import requests
import json
from twilio.rest import Client
import wolframalpha
from selenium import webdriver
from time import sleep

warnings.filterwarnings("ignore")
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
def talk(audio):
    engine.say(audio)
    engine.runAndWait()
#talk("This would be the test")
def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("I'm on the way listening it...")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You just spelled: "+data)

    except sr.UnknownValueError:
        print("Assistant could not sense it...")

    except sr.RequestError as ex:
        print("Request error from google speech recognition"+ex)

    return data
def response(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)
def call(text):
    action_call= " dear assistant"
    text=text.lower()
    if action_call in text:
        return True
    return False
def today_date():
    now= datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months=["january","february","march","april","may","june","july","august","september","october","november","december"]
    ordinals=["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","2th","28th","29th","30th","31st"]
    return f'Today is {week_now},{months[month_now -1]} the {ordinals[day_now -1]}.'
def say_hello(text):
    greet = ["hi","hello","hola","howdy","hey there", "how are you"]
    response = ["hi","hello","hola","howdy","hey there", "i'm doing good"]
    for word in text.split():
        if word.lower()in greet:
            return random.choice(response)+"."
    return ""
def wiki_person(text):
    list_wiki = text.split()
    for i in range(0,len(list_wiki)):
        if i +3 <= len(list_wiki) -1 and list_wiki[i].lower()=="who" and list_wiki[i+1].lower()=="is":
            return list_wiki[i+2]+" "+list_wiki[i+3]
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-")+"-note.txt"
    with open(file_name,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])
def send_email(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("emailid","password")
    server.sendmail("emailid",to,content)
    server.close()
def pizza():
    driver = webdriver.Chrome(
        r"C:\...\chromedriver.exe"  # Location of your webdriver
    )
    driver.maximize_window()  # Maximizes the browser window

    talk("Opening Dominos")
    driver.get('https://www.dominos.co.in/')  # Open the site
    sleep(2)

    talk("Getting ready to order")
    driver.find_element_by_link_text('ORDER ONLINE NOW').click()  # Click on order now button
    sleep(2)

    talk("Finding your location")
    driver.find_element_by_class_name('srch-cnt-srch-inpt').click()  # Click on the location search
    sleep(2)

    location = ""  # Enter your location

    talk("Entering your location")
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input').send_keys(
        location)  # Send text to location search input field
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]').click()  # Select the location from suggestions
    sleep(2)

    try:
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]').click()  # Click on login button
        sleep(2)
    except:
        talk("Your location could not be found. Please try again later.")
        exit()

    talk("Logging in")
    phone_num = ""  # Enter your phone number here

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(
        phone_num)  # Send text to phone number input field
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
    sleep(2)

    talk("What is your O T P? ")
    sleep(3)

    otp_log = rec_audio()

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(
        otp_log)  # Paste the OTP into the text field
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()  # Submit OTP
    sleep(2)

    talk("Do you want me to order from your favorites?")
    query_fav = rec_audio()

    if "yes" in query_fav:
        try:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[6]/div/div/div[2]/div[3]/div/button/span').click()  # Add your favorite pizza
            sleep(1)
        except:
            talk("The entered OTP is incorrect.")
            exit()

        talk("Adding your favorites to cart")
        talk("Do you want me to add extra cheese to your pizza?")
        ex_cheese = rec_audio()
        if "yes" in ex_cheese:
            talk("Extra cheese added")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[2]/button').click()  # Add extra cheese
        elif "no" in ex_cheese:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
        else:
            talk("I dont know that")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()

        driver.find_element_by_xpath(
            '//*[@id="mn-lft"]/div[16]/div/div[1]/div/div/div[2]/div[2]/div/button').click()  # Add a pepsi
        sleep(1)

        talk("Would you like to increase the qty?")
        qty = rec_audio()
        qty_pizza = 0
        qty_pepsi = 0
        if "yes" in qty:
            talk("Would you like to increase the quantity of pizza?")
            wh_qty = rec_audio()
            if "yes" in wh_qty:
                talk("How many more pizzas would you like to add? ")
                try:
                    qty_pizza = rec_audio()
                    qty_pizza = int(qty_pizza)
                    if qty_pizza > 0:
                        talk_piz = f"Adding {qty_pizza} more pizzas"
                        talk(talk_piz)
                        for i in range(qty_pizza):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]').click()
                except:
                    talk("I dont know that.")
            else:
                pass

            talk("Would you like to increase the quantity of pepsi?")
            pep_qty = rec_audio()
            if "yes" in pep_qty:
                talk("How many more pepsis would you like to add? ")
                try:
                    qty_pepsi = rec_audio()
                    qty_pepsi = int(qty_pepsi)
                    if qty_pepsi > 0:
                        talk_pep = f"Adding {qty_pepsi} more pepsis"
                        talk(talk_pep)
                        for i in range(qty_pepsi):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]').click()
                except:
                    talk("I dont know that.")
            else:
                pass

        elif "no" in qty:
            pass

        total_pizza = qty_pizza + 1
        total_pepsi = qty_pepsi + 1
        tell_num = f"This is your list of order. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
        talk(tell_num)
        check_order = rec_audio()
        if "yes" in check_order:
            talk("Checking out")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button').click()  # Click on checkout button
            sleep(1)
            total = driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[6]/span[2]/span')
            total_price = f'total price is {total.text}'
            talk(total_price)
            sleep(1)
        else:
            exit()

        talk("Placing your order")
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[8]/button').click()  # Click on place order button
        sleep(2)

        talk("Saving your location")
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input').click()  # Save your location
        sleep(2)

        talk("Do you want to confirm your order?")
        confirm = rec_audio()
        if "yes" in confirm:
            try:
                driver.find_element_by_xpath(
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
                sleep(2)
            except:
                talk("The store is currently offline.")
                exit()

            talk("Placing your order")

            talk("Your order is places successfully. Wait for Dominos to deliver your order. Enjoy your day!")
        else:
            exit()

    else:
        exit()

while True:
        try:
            text= rec_audio()
            speak=" "
            if call(text):
                speak=speak+ say_hello(text)
                if "date" in text or "day" in text or "month" in text:
                    get_today = today_date()
                    speak = speak +" "+ get_today
                elif "time" in text:
                    now= datetime.datetime.now()
                    meridiem = ""
                    if now.hour >=12:
                        meridiem = "p.m"
                        hour = now.hour -12
                    else:
                        meridiem ="a.m"
                        hour=now.hour
                    if now.minute <10:
                        minute = "0"+ str(now.minute)
                    else:
                        minute= str(now.minute)
                    speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."
                elif "wikipedia" in text or "Wikipedia" in text:
                    if "who is" in text:
                        person = wiki_person(text)
                        wiki= wikipedia.summary(person,sentences=2)
                        speak = speak+" "+ wiki
                elif "who are you" in text or "define yourself" in text or "may i know who are you" in text:
                    speak = speak + "Hello,I am your dear assistant.I am here to assist you and make you feel better"
                elif "your name" in text:
                    speak = speak + "Hello,my name is dear assistant"
                elif "who am i " in text:
                    speak = speak + "You must probably be a human"
                elif "why do you exist" in text or "how do you exist" in text:
                    speak = speak + "It is a secret"
                elif "how are you" in text:
                    speak = speak + "I am fine, thank you"
                    speak = speak + "\n How are you?"
                elif "fine" in text or "good" in text:
                    speak = speak + "great, good to know that."
                elif "open" in text:
                    if "chrome" in text.lower():
                        speak = speak + "Opening Google Chrome"
                        os.startfile(
                            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                        )
                    elif "word" in text.lower():
                        speak = speak + "opening Microsoft word"
                        os.startfile(
                            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                        )
                    elif "excel" in text.lower():
                        speak = speak + "opening Microsoft excel"
                        os.startfile(
                            r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                        )
                    elif "document" in text.lower():
                        speak = speak + "opening pdf reader"
                        os.startfile(
                            r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
                        )
                    elif "vs code" in text.lower():
                        speak = speak + "opening vs code"
                        os.startfile(
                            r"C:\Users\USER\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                        )
                    elif "powerpoint" in text.lower():
                        speak = speak + "opening powerpoint"
                        os.startfile(
                            r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
                        )
                    elif "youtube" in text.lower():
                        speak = speak + "opening youtube"
                        webbrowser.open("https://www.youtube.com/")
                    elif "amazon" in text.lower():
                        speak = speak + "opening amazon"
                        webbrowser.open("https://www.amazon.com/")
                    else:
                        speak = speak + "sorry, I can't find the application."
                elif "youtube" in text.lower():
                    ind = text.lower().split().index("youtube")
                    search = text.split()[ind+1:]
                    webbrowser.open("https://www.youtube.com/results?search_query="+"+".join(search))
                    speak = speak + "opening"+str(search)+"on youtube"
                elif "search" in text.lower():
                    ind = text.lower().split().index("search")
                    search = text.split()[ind + 1:]
                    webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                    speak = speak + "opening" + str(search) + "on google"
                elif "google" in text.lower():
                    ind = text.lower().split().index("google")
                    search = text.split()[ind + 1:]
                    webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                    speak = speak + "opening" + str(search) + "on google"
                elif "change background" in text or "change wallpaper" in text:
                    img= r'C:\Users\DEON\Desktop\Wallpapers'
                    list_img = os.listdir(img)
                    imgChoice = random.choice(list_img)
                    randomImg = os.path.join(img,imgChoice)
                    ctypes.windll.user32.SystemParametersInfoW(20, 0,randomImg,0)
                    speak=speak + "Background changed successfully"
                elif "play music" in text or "play song" in text:
                    talk("Here you go with music")
                    music_dir = r'C:\Users\DEON\Desktop\Music'
                    songs = os.listdir(music_dir)
                    d = random.choice(songs)
                    random = os.path.join(music_dir,d)
                    playsound.playsound(random)
                elif "empty recycle bin" in text:
                    winshell.recycle_bin().empty(
                        confirm=True, show_progress=False, sound=True
                    )
                    speak = speak+"recycle bin emptied"
                elif "note" in text or "remember this" in text:
                    talk("what would you like me to write down ?")
                    note_text = rec_audio()
                    note(note_text)
                    speak = speak + "I have made a note of that"
                elif "joke" in text or "jokes" in text:
                    speak = speak + pyjokes.get_joke()
                elif "where is" in text:
                    ind = text.lower().split().index("is")
                    location = text.split()[ind+1:]
                    url="https://www.google.com/maps/place/"+"".join(location)
                    speak = speak + "This is where" + str(location)+"is."
                    webbrowser.open(url)
                elif "email to computer" in text or "gmail to computer" in text:
                    try:
                        talk("what should i say")
                        content = rec_audio()
                        to = "reciever email address"
                        send_email(to,content)
                        speak=speak+"Email has been sent"
                    except Exception as e:
                        print(e)
                        talk("I am not able to send this email")
                elif "mail" in text or "email" in text or "gmail" in text:
                    try:
                        talk("what should i say")
                        content = rec_audio()
                        talk("whom should i send")
                        to = input("Enter to address: ")
                        send_email(to,content)
                        speak = speak + "Email has been sent!"
                    except Exception as e:
                        print(e)
                        speak = speak + "I am not able to send this email  "
                elif "weather" in text or "atmosphere" in text:
                    key="da18b5ab92a8b9312506aa6a03e13317"
                    weather_url = "https://api.openweathermap.org/data/2.5/weather?"
                    ind = text.split().index("in")
                    location = text.split()[ind + 1:]
                    location = "".join(location)
                    url = weather_url + "appid" + key + "&q=" + location
                    js = requests.get(url).json()
                    if js["cod"] != "404" :
                        weather = js["main"]
                        temperature = weather["temp"]
                        temperature = temperature - 273.15
                        humidity = weather["humidity"]
                        desc = js["weather"][0]["description"]
                        weather_response = "The temperature in Celcius is"+str(temperature)+"The humidity is"+str(humidity)+"and by the way weather description is"+str(desc)
                        speak = speak + weather_response
                    else:
                        speak = speak + "City not found"
                elif "news" in text or "current affairs" in text:
                    url = ('https://newsapi.org/v2/everything?'
                           'q=Apple&'
                           'from=2023-01-16&'
                           'sortBy=popularity&'
                           'apiKey=546dff61a04446c58f546c7088807d61')
                    try:
                        response = requests.get(url)
                    except:
                        talk("please check your connection")
                    news = json.loads(response.text)
                    for new in news["articles"]:
                        print(str(new["title"]), "\n")
                        talk(str(new["title"]))
                        engine.runAndWait()

                        print(str(new["description"]),"\n")
                        talk(str(new["description"]))
                        engine.runAndWait()
                elif "send message" in text or "send a message" in text:
                    account_sid="AC7f4698ad570e516a01356bb9a7ebae9c"
                    auth_token="c152bcfcb0f317e3e0a7236bcaee72a5"
                    client = Client(account_sid, auth_token)

                    talk("What should i send")
                    message = client.messages.create(
                        body=rec_audio(), from_="+12028661521", to="+919553327627"
                    )
                    print(message.sid)
                    speak = speak+"Message sent successfully"
                elif "calculate" in text:
                    app_id = "982W7U-V4E2GH83WJ"
                    client = wolframalpha.Client(app_id)
                    ind = text.lower().split().index("calculate")
                    text = text.split()[ind+1:]
                    res = client.query("".join(text))
                    answer = next(res.results).text
                    speak = speak +"The answer is" + answer
                elif "what is" in text or "who is" in text:
                    app_id = "982W7U-V4E2GH83WJ"
                    client = wolframalpha.Client(app_id)
                    ind = text.lower().split().index("is")
                    text = text.split()[ind + 1:]
                    res = client.query("".join(text))
                    answer = next(res.results).text
                    speak = speak + "The answer is" + answer
                elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
                    talk("for how many seconds do you want me to stop listening")
                    a = int(rec_audio())
                    speak+="I will be back in"+str(a)+"seconds."
                    time.sleep(a)
                    speak+=str(a)+"seconds completed.Now I am ready to assist you"
                elif "exit" in text or "quit" in text:
                    exit()
                elif "order a pizza" in text or "pizza" in text:
                    pizza()





                response(speak)
        except:
            talk("I'm sorry, I don't know that")
