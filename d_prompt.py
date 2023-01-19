li=[]
n=int(input("enter the limit"))
for i in range(n):
    el=int(input("enter the number"))
    if el>100:
        el="over"
    li.append(el)
print(li)

