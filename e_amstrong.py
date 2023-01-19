
num=int(input("enter the number"))
copy=num
sum=0
for i in range(0,len(str(num))):
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10

if sum==copy:
    print(copy,"is an amstrong number")
else:
    print(copy, "is not an amstrong number")
