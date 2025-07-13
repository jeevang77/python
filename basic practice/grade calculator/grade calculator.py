sub1 = int(input ("enter your marks in sub1:"))
sub2 = int(input ("enter your marks in sub2:"))
sub3 = int(input ("enter your marks in sub3:"))
sub4 = int(input ("enter your marks in sub4:"))

total_marks = sub1+sub2+sub3+sub4
average_marks = total_marks / 4

percentage = (total_marks/400)*100

if percentage >= 90 :

    print("grade A+")

elif percentage < 90 and percentage >= 80 :

    print("grade A")

elif percentage < 80 and percentage >= 75 :

    print("grade B")

elif percentage < 75 and percentage >= 50 :

    print("grade C")

elif percentage < 50 :

    print("fail")

print(f" total_marks:{total_marks} \n average marks:{average_marks} \n percentage:{percentage}")




