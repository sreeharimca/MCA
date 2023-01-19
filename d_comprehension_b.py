num=int(input("enter the limit"))
li=[]
for i in range(num):
    a=int(input("enter the element"))

    li.append(a)

newli=[i*i for i in li if i>0]
print("the squares are",newli)


