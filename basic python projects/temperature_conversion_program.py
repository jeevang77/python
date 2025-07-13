# temperature conversion program

temp = float(input("enter temperature in your area: "))
unit = input("what is the unit of temperature (C or F) in capitals: ")

if unit == "C":
    temp = round((temp * 9)/5 + 32, 1)
    unit = "F"
    print(f"temperature in  your area is: {temp} {unit}")

elif unit == "F":
    temp = round((temp - 32)/(9/5), 1)    
    unit = "c"
    print(f"temperature in  your area is: {temp} {unit}")

else :
    print(f"{unit} : you have entered a wrong unit of measurement")