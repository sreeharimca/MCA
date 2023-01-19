n=input("enter the string").split(' ')
li=list(n)

set=set(li)

newli=list(set)
for i in newli:
    count=0
    for j in li:
        if i==j:
            count=count+1
    print("occurance of ",i,count)