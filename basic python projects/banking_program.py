
# Banking program

def show_balance () :
    print("------------------->")
    print(f"your balance in your account is {balance}")
    print("------------------->")

def deposit () :
    print("------------------->")
    amount = float(input("enter the amount you want to deposit: "))
    print("------------------->")
    if amount < 0 :
        print("amount can't be less than 0")
        return 0                                                # return 0 for doesn't change in the balance and doesn't crash the program if we enter negative numbers
    else :
        return amount                                           # returns valid amount
    
def withdraw () :
    print("------------------->")
    amount = float(input("enter the amount you want to withdraw: "))
    print("------------------->")
    if amount < 0:
        print("amount can't be less than 0")
        return 0                                                  # return 0 for doesn't change in the balance and doesn't crash the program if we enter negative numbers
    elif amount > balance :
        print("insufficinet funds")                                                               
    else :
        return amount                                            # returns valid amount

balance = 0
is_running = True

while is_running :
    print("--------------banking problem--------------")
    print("1.show balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
    print("-------------------------------------------")

    choice = input("enter your choice(1-4): ")
    
    match choice :                                              # using match-case statements
        case "1" :
            show_balance()
        case "2" :
            balance += deposit()
        case "3" :
            balance -= withdraw()
        case _ :
            is_running = False
print("------------------->")
print("Thank you!, have a nice day")
print("------------------->")