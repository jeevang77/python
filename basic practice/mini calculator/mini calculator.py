# mini calculator using operators and conditional statements

num1=int(input("enter 1st number:"))

num2=int(input("enter 2nd number:"))

oper=input("enter the operator:").lower()

if oper == "addition" or oper == "+" :

    print("addition:" ,num1+num2)

elif oper == "subtraction " or oper == "-" :

    print("subtraction:" ,num1-num2)

elif oper == "multiplication " or oper == "*" :

    print("multiplication:" ,num1*num2)

elif oper == "division" or oper == "/" :

    if num1 =="0" or num2 =="0":

        print("division with zero is not possible")

    else:

        print("division:" ,num1/num2)

elif oper == "floor division" or oper == "//" :

    
    if num1 =="0" or num2 =="0":

        print("floor division with zero is not possible")

    else:

        print(f"floor division: {num1//num2}")     #  used f string


elif oper == "exponentiation" or oper == "**" :

        print(f"exponentiation: {num1**num2}")


elif oper == "modulous" or oper == "%" :

    if num1 =="0" or num2 =="0":

        print("modulous with zero is not possible")

    else:

        print(f"modulous: {num1%num2}")







  

  