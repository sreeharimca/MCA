li=[]
num=int(input("enter the number of elements"))
m=0
for i in range(num):
    l=input("enter the name")
    li.append(l)
for i in li:
    c=i.count("a")
    m=m+c

print("count of a is ",m)

