
## shopping cart program


foods = []
prices = []
total_price = 0

while True :

    food = input("enter the name of the food (q to quit): ")

    if food.lower() == "q":
        break        

    else:

        price = float(input("enter the price of the food: "))
        foods.append(food)
        prices.append(price)

print("----------------------YOUR CART-------------------------")


my_dict = dict(zip(foods,prices))

for food,price in my_dict.items() :
    print(f"{food}: {price}")

for price in prices :
    total_price += price

print(f"total price of the food is ₹{round(total_price, 2)}")