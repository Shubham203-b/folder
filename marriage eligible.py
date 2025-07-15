#marriage calculator
print("enter the 1 if you are a male \nenter the 2 for if you are female ")
g=int(input("Enter you gender as a number: "))
if g==1:
    a=int(input("enter you age: "))
    if a>=21:
        print("you are eligible for marriage ")
    else:
        print("you are not eligible for marriage")
elif g==2:
    a=int(input("Enter your age: "))
    if a>=18:
        print("you are eligible for marriage")
    else:
        print("you are not eligible for marriage")