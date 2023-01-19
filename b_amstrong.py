num=int(input("enter the value"))
sum=0
copy=num
while(num>0):
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10
if sum==copy:
    print(copy,"is an amstrong number")
else:
    print(copy,"is not an amstrong number")

