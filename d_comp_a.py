num=int(input("enter the limit"))
li=[]
for i in range(num):
    a=int(input("enter the element"))

    li.append(a)
print("the list you entered is:",li)
newli=[i for i in li if i>0]
print("the new list is",newli)

