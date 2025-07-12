name = input("enter a name:").lower()

a = name.count("a")
e = name.count("e")
i = name.count("i")
o = name.count("o")
u = name.count("u")

print(f"number of vowels in your name :{a+e+i+o+u}")