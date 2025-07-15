#water calcualtor ;
a=int(input("enter the  water bottle you have : "))
b=int(input("enter the bottle you have to drink water bottle per day : "))
res=a-b
x=1
while res >= 1:
    print(x,"Day : water bottle present : ",res,)
    x+=1
    res-=b

print("no more bottle present")