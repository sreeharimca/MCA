num=int(input("enter the number"))
sum=0
for i in range(0,len(str(num))):
    rem=num%10
    sum=(sum*10)+rem
    num=num//10
print("the reverse is",sum)



