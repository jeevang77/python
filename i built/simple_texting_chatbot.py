# simple texting chat bot
# we use conditional statements and loops in this chatbot

user_name = None
chatbot = "spideybot"


print("---------------------------------")
print("hey ! i am your friendly chatbot ")
print("---------------------------------")

chatting = True

while chatting :

    chat = input("user: ").lower().strip()

    if "my name is " in chat :
        user_name = chat.split("my name is ")[-1].strip()
        print(f"hey {user_name}, that's a great name i like it")

    elif chat in ["hi", "hello", "hey"] :
        if user_name :
            print(f"chatbot: {chat}, i'm excited to see you here {user_name} and i'm here to help you ask me  ")
        else :
            print(f"chatbot: {chat}, i'm excited to see you here and i'm here to help you ask me  ")

    elif chat in ["what is your name", "name", "may i know your name","your name"] :
        if user_name :
            print(f"chatbot: my name is {chatbot}, {user_name}")
        else :
            print(f"chatbot: my name is {chatbot} , may i know about yours")

    elif chat in ["how are you","how are you doing"] :
        if user_name :
            print(f"hey {user_name} im doing great and i feel very exciting talking to you ")
        else :
            print(f"hey im doing great and i feel very exciting talking to you ")

    elif chat in ["bye", "see you"] :
        if user_name :
            print(f"{chat} {user_name}, great talking you i would like to see you again")
        else :
            print(f"{chat} , great talking you i would like to see you again")
        chatting = False

    else :
        print("i dont understand this ")

    
               
print("---------------------------------")
print("thank you for using spideybot")
print("---------------------------------")



