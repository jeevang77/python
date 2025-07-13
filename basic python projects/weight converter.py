
# weight converter program


weight = float(input("enter your weight: "))
unit = input("Kilograms or Pounds (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is {round(weight), 1} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"your weight is {round(weight), 1} {unit}")

else:
    print(f"you have entered a wrong unit {unit}")