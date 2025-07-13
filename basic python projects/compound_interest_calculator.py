# compund interest calculator
# formula 
# final amount = principal * (1+(rate/n))**time



principle = 0
interest_rate = 0
time = 0

while True:
    principle = float(input("enter principle amount: "))
    if principle <= 0 :
        print("principle can not be 0 or less tha 0")
    else:
        break

while True :
    interest_rate = float(input("enter interest_rate: "))
    if interest_rate <= 0 :
        print("interest_rate can not be 0 or less tha 0")
    else:
        break

while True:
    time = float(input("enter time in years"))
    if time <= 0 :
        print("time can not be 0 or less tha 0")
    else:
        break

final_amount = principle * (1+(interest_rate/100))**time

print(f"the balance after {time} years is ₹{round(final_amount, 2)}")



