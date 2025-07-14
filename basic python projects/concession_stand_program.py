# concession stand program


menu ={"Chips" : 50,
       "Coke" : 40,
       "Fried Chicken" : 200,
       "French Fries" : 100,
       "Burger" : 170,
       "Pizza" : 250,
       "Pasta" : 150,
       "Fish" : 200}

cart = []
total_price = 0

print("--------------------MENU-----------------")

for key,value in menu.items() :
    print(f"{key:15}: ₹{value:.2f}")

print("-----------------------------------------")


while True :
    food = input("enter the name of the food (q to quit): ").title()
    if food.lower() == "q" :
        break
    elif food in menu :
        cart.append(food)
    else:
        print("your order is not in menu ")
        
print("--------------------YOUR ORDER-----------------")

for food in cart :
    print(food,end=(" "))
    print()
    total_price += menu.get(food)

print("-----------------------------------------------")

    

print(f"your total price of the food is: {total_price}")
