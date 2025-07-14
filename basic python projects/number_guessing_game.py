# Number guessing game

import random


lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)

guesses = 0

print("----------number guessesing game---------")

print(f"please select a number between {lowest_num} and {highest_num}")

print("-----------------------------------------")
while True :
    guess = int(input(f"enter your guess in between {lowest_num} and {highest_num}: "))
    
    if guess > highest_num or guess < lowest_num :
        print("invalid guess")
        print(f"please enter your guess in between {lowest_num} and {highest_num} ")

    else:
        guesses +=1

        if guess < answer :
            print(f"{guess} is too low!, try again")

        elif guess > answer :
            print(f"{guess} is too high!, try again")

        else:
            print(f"correct the answer is {answer}")
            print(f"the no of guesses is {guesses}")