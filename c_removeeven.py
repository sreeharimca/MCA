n=int(input("enter the limit"))
li=[]
for i in range(n):
    element=int(input("enter the element"))
    li.append(element)
print(li)
for i in li:
    if(i%2==0):
        li.remove(i)
print("list after removing  even numbers",li)