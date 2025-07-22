

import speech_recognition as sr
import time
import webbrowser
import os
import playsound
from gtts import gTTS
import random
import yfinance as yf


# Keywords for different functionalities
# These keywords will be used to identify the user's intent from their speech input

search_keywords = ["search for","look for","google","what is","how to","tell me about","can you","please","look up for","the definition of","for me"]
youtube_keywords = ["search for", "on youtube", "in youtube","play","video",'watch',"i would like to","can you","please","open the","for me"]
map_keywords = ["find the location of","search for","search the location of","the location of","what's","where is","show me"]
exit_keywords = ["exit", "quit", "see you", "see ya", "see you later", "goodbye", "bye","talk to you later", "catch you later", "thanks, bye",]
stock_price_keywords = ["tell me the","stock","share", "current","price of", "current share price","what's the"]


r = sr.Recognizer()

person_name = ""

def listen_to_user():
    with sr.Microphone() as source:
        r.pause_threshold = 0.6        # Allows brief pauses while talking
        r.dynamic_energy_threshold = False
        r.energy_threshold = 500       # Adjust if background noise is high
        r.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        audio = r.listen(source, timeout=None, phrase_time_limit=None)
        print("Processing...")
        prompt = ""
        print(prompt)
        try:
            prompt = r.recognize_google(audio, language='en-US').lower().strip()
            print(prompt)
        except sr.UnknownValueError:
            spidey_speak("sorry, i don't understand that")
        except sr.RequestError:
            spidey_speak("sorry, my speech service is down")
        return prompt


def spidey_speak(audio):
    tts = gTTS(text=audio, lang='en')
    r = random.randint(1, 2000000)
    audio_file = "audio" + str(r) + ".mp3"
    tts.save(audio_file)
    print(audio)
    playsound.playsound(audio_file)
    os.remove(audio_file)

 

def respond(prompt):

    prompt = prompt.lower().strip()

    global person_name

    if prompt in ["hello", "hi", "hey"]:
        if person_name:
            spidey_speak(f"hey, how can I help you {person_name}")
        else:
            spidey_speak("hey there, good to see you here, how can i help you")

    elif prompt in ["what is your name", "your name", "who are you", 'name',"what's your name"]:
        if person_name:
            spidey_speak(f"my name is spidey, {person_name}")
        else:
            spidey_speak("my name is spidey,may i know your name?")

    elif prompt in ["time", "what time is it", "what's the time now","what's the time"]:
        if person_name:
            spidey_speak(f"the current time is {time.ctime()}, {person_name}")
        else:
            spidey_speak("the current time is " + time.ctime())

    elif "my name is" in prompt:
        person_name = prompt.split("is")[-1].strip()
        spidey_speak(f"okay, i will remember that {person_name}")

    elif any(word in prompt for word in search_keywords) and "youtube" not in prompt : 
        search_term = prompt
        for word in search_keywords :
            if word in prompt :
                search_term = search_term.replace(word,"").strip()        
        if not search_term :
            spidey_speak("What would you like me to search?")
            search_term = listen_to_user()
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.get().open(url)
        spidey_speak(f"here is what i found for {search_term} on google")

    elif any(word in prompt for word in youtube_keywords) and "youtube" in prompt or "video" in prompt or "watch" in prompt :
        search_term =prompt
        for word in youtube_keywords :
                search_term = search_term.replace(word,"").strip()
        if not search_term :
            spidey_speak("What would you like me to search on youtube?")
            search_term = listen_to_user()
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        spidey_speak(f"here is what i found for {search_term} on youtube")

    elif any(word in prompt for word in map_keywords) and "location" in prompt :
        search_term = prompt
        for word in map_keywords :
                search_term = search_term.replace(word,"").strip()
        if not search_term :
            spidey_speak("which location are you looking for?")
            search_term = listen_to_user()
        url = f"https://www.google.com/maps/place/{search_term}/"
        webbrowser.get().open(url)
        spidey_speak(f"here is what i found for {search_term} on google maps")

    elif any(word in prompt for word in stock_price_keywords):
        search_term = prompt
        for word in stock_price_keywords:
            search_term = search_term.replace(word, "").strip()
        stocks = {
            "apple":"AAPL",
            "microsoft":"MSFT",
            "facebook":"FB",
            "tesla":"TSLA",
            "bitcoin":"BTC-USD"}
        
        if search_term in stocks :
            try:
                stock_symbol = stocks[search_term]
                stock = yf.Ticker(stock_symbol)
                price = stock.info["regularMarketPrice"]
                currency = stock.info["currency"]
                spidey_speak(f"The current price of {search_term} is {price} {currency}")
            except :
                spidey_speak("Sorry, I couldn't fetch the stock price right now.")
        else :
            spidey_speak("please specify a valid stock name")

    elif any(word in prompt for word in exit_keywords):
        spidey_speak("going offline,see you later")
        exit()                     

time.sleep(1)

while (1):
    prompt = listen_to_user()
    respond(prompt)
