num1,num2=0,1
r=int(input("enter the range"))
for i in range(r):
    print(num1,end='   ')
    temp=num1+num2
    num1=num2
    num2=temp
