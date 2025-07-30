# simple texting chatbot program
# We use functions, conditional statements, and loops in this chatbot program to enhance its readability and structure. 


user_name = None
chatbot = "spideybot"

def set_user_name(chat) :
  global user_name
  name = chat.split("my name is")[-1].strip()
  if name :
    user_name = name
    print(f"chatbot: {user_name} that's a great name, i like it ")
    return user_name
  else :
    print("I didn't catch your name. Could you repeat that?")

def greeting(chat) :
  if user_name :
    print(f"chatbot: {chat} {user_name}, nice to see you here")
  else :
    print(f"chatbot: {chat},nice to see you here")

def feeling(chat) :
  if user_name :
    print(f"chatbot: I am fine{user_name}, thank you!")
  else :
    print(f"chatbot: I am fine, thank you!")

def bot_name() :
  if user_name :
    print(f"chatbot: my name is {chatbot}, {user_name}")
  else :
    print(f"chatbot: my name is {chatbot}, may i know your's")

def exit_chat(chat) :
  if user_name :
    print(f"chatbot: {chat} {user_name}, it was nice talking to you!")
  else :
    print(f"chatbot: {chat}, it was nice talking to you!")

def unknown() :
  print("chatbot: i don't understand this, i'm still learning")


print("---------------------------------")
print("Hey! I am your friendly chatbot")
print("---------------------------------")

chatting = True

while chatting :
  chat = input("user: ").lower().strip()

  if chat in ["hi", "hello", "hey"] :
    greeting(chat)

  elif chat in ["how are you", "how are you doing"] :
    feeling(chat)

  elif "my name is" in chat :
    set_user_name(chat)

  elif chat in ["what is your name", "what is your name?", "your name"] :
    bot_name()

  elif chat in ["bye", "goodbye", "see you later"] :
    exit_chat(chat)
    chatting = False

  else :
    unknown()

print("---------------------------------")
print("thank you! for using spideybot")
print("---------------------------------")
