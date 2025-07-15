# multiple time calcualtor
a=int(input("enter the number  "))
c=1
while c<5 and c>0 :
            print("Enter 1 = addition(+)\n 2 = subtraction(-)\n 3 = multiplication(*)\n 4 = division(/)\n large and equal than 5 number for close of calculation ")
            c=int(input("enter the calculation symble number: "))
            b=int(input("enter the number "))
            if c==1:
                   print("answer : ",a+b)
            elif c==2: print("answer : ",a-b)
            elif c==3: print("answer : ",a*b)
            elif c==4: print("answer : ",a/b)
            else:
                    print("error!!!!!!")
                    break
            print("Enter again for calculation")