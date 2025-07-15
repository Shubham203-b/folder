#tip ,split bill amount in persons. restaurant simulator
print("this is for give tip as with bill percentage  and  bill amount split in persons\n\t\ta restaurant simulator")
a=int(input("Enter the amount of bill: "))
print("Enter the 1 - Number if you give tip from bill amount percentage\nEnter the 2 - Number if you want split bill amount in persons")
b=int(input("Enter the number : "))
if b==1:
    t=int(input("Enter the number : "))
    if t<=50: print((t*a)/100)
    else: print("10% to 50% tip of bill amount only ")
elif b==2:
    p=int(input("Enter the number of Person : "))
    print(a/p," for bill amount for each person")
else :print("number error!!! please enter only 1,2 Number")