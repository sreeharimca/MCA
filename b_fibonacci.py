limit=int(input("enter the limit"))
first=0
second=1
sum=0
print(first)
i=1
while(i<limit):
    first=second
    second=sum
    sum=first+second
    i+=1
    print(sum)