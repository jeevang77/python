# rock , paper , sicssors game 


import random

print(" welcome to rock , paper , scissors game \n rules- \n if rock vs paper : paper wins paper covers rock \n if rock vs scissors : rock wins rock smashes scissors \n if paper vs scissors : scissors wins scissors cuts paper ")

options = ("rock" , "paper" , "scissors")
running = True

playerscore = 0
computerscore = 0
ties = 0


while running :

    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("enter a choice (rock , paper, scissors): ").lower()
        
        
    print(f"player choice : {player}")
    print(f"computer choice : {computer}")



    if player == "rock" and computer == "scissors" :
        print("player wins!")
        playerscore += 1

    elif player == "paper" and computer == "rock" :
        print("player wins!")
        playerscore += 1

    elif player == "scissors" and computer == "paper" :
        print("player wins!")
        playerscore += 1

    elif player == computer :
        print("its a tie")
        ties +=1

    else :
        print("computer wins!")
        computerscore += 1     
     
    play_again = input("you want to play again (yes or no): ").lower()
    if play_again == "yes" :
        continue
    else :
        running = False


print("---------------------RESULTS------------------")
print()
print("thanks for playing!")
print(f"player wins is {playerscore}\n computer wins is {computerscore}\n ties are {ties}")
