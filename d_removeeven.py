n=int(input("enter the limit"))
li=[]
for i in range(n):
    num=int(input("enter the number"))
    li.append(num)
print(li)
for i in li:
    if i%2==0:
        li.remove(i)
print("list after removing even",li)
