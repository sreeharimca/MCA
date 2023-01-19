n=int(input("enter the limit"))
li=[]
for i in range(n):
    num=int(input("enter the number"))
    li.append(num)
sum=0
for i in li:
    sum=sum+i
print("The sum is",sum)