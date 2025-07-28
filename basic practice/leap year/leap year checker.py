year = int (input("enter the year:"))

leap = False

if year%400 == 0 :
    leap = True
elif  year%100 == 0 :
    leap = False
elif year%4 ==0 :
    leap = True

else:
    leap = False

print(leap)