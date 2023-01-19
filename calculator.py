print("enter the operation to perform")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
num1=int(input("enter first number"))
num2=int(input("enter second number"))
choice=int(input("enter your choice"))
if choice in(1,2,3,4):
    if choice==1:
        print(num1,'+',num2,'=',num1+num2)
    elif(choice==2):
        print(num1,'-',num2,'=',num1-num2)
    elif(choice==3):
        print(num1,'*',num2,'=',num1*num2)
    elif(choice==4):
        print(num1,'/',num2,'=',num1/num2)
else:
    print("enter a valid choice")
