# printing numbers from 1 to n using while and for loops

n = int ( input ( " enter the value of n:"))
i=1
while i <=n :
    print(i)
    i+=1


n = int ( input ( " enter the value of n:"))
for i in range (1,n+1):
    print(i)


# printing sum of n natural numbers using for and while loops

n = int ( input ( " enter the value of n:"))
i=1
sum=0
while i <=n :
    sum+=i
    i+=1
print(sum)


n = int ( input ( " enter the value of n:"))
sum = 0
for i in range (1,n+1):
    sum+=i
print(sum)


# printing factorial of a number using while and for loops

n = int ( input ( " enter the value of n:"))
i=1
factorial = 1
while i<=n :
    factorial = factorial * i
    i+=1
print(factorial)


n = int ( input ( " enter the value of n:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial * i
print(factorial)



# printing even numbers using while and for loops

n = int ( input ( " enter the value of n:"))
i=1
while i <= n:
    if i%2 == 0:
        print(i)
    i+=1


n = int ( input ( " enter the value of n:"))

for i in range(1,n+1):
    if i%2 ==0:
        print(i)




# printing odd numbers using while and for loops

n = int ( input ( " enter the value of n:"))
i=0
while i <= n:
    if not (i%2 == 0):
        print(i)
    i+=1



n = int ( input ( " enter the value of n:"))

for i in range(1,n+1):
    if i%2 !=0:
        print(i)




 # printing tabulous form using while and for loops


n = int ( input ( " enter the value of n:"))
i=1
while i<=n:
    print(f"{n} * {i} = {n *i}")
    i+=1



n = int ( input ( " enter the value of n:"))
for i in range(1,n+1):
    print(f"{n} * {i} = {n *i}")


