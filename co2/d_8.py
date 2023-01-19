n=int(input("enter the limit"))
a=[]
for i in range(n):
    num=input("enter the string")
    a.append(num)

max1 = len(a[0])
temp = a[0]

for i in a:
    if (len(i) > max1):
        max1 = len(i)
        temp = i

print("longest word is", temp," and length is ", max1)