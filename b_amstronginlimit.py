num1=int(input("enter the first limit"))
num2=int(input("enter the last limit"))
sum=0

while(num1<num2):
    rem=num1%10
    sum=sum+(rem*rem*rem)
    num1=num1//10
print(sum)



