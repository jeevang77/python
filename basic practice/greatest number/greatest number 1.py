num_1,num_2,num_3 = input('enter three numbers:').split(",")     # used string method

greatest = 0


if num_1 > num_2 and num_1 > num_3 :

    greatest = num_1

elif num_2 > num_1 and num_2 > num_3 :

    greatest = num_2

elif num_3 > num_1 and num_3 > num_2 :

    greatest = num_3

elif num_1 == num_2 and num_1 == num_3 :
     
     print("all numbers are equal")

print(greatest)