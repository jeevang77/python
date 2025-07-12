#checking if the word is palindrome



name =input("enter a name").lower()


if name==name[::-1]:
    print("yes it is a palindrome")

else:
    print("it is not a palindrome")