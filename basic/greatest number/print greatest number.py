num_1 = int(input('enter 1st number:'))
num_2 = int(input('enter 2nd number:'))
num_3 = int(input('enter 3rd number:'))


if num_1 > num_2 and num_1 > num_3 :

    print(f"1st number is greatest:{num_1}")

elif num_2 > num_1 and num_2 > num_3 :

    print(f"2nd number is greatest:{num_2}")

elif num_3 > num_1 and num_3 > num_2 :

    print(f"3rd number is greatest:{num_3}")

elif num_1 == num_2 and num_1 == num_3 :
     
     print("all numbers are equal")