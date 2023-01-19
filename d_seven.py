n=int(input("enter the limit"))
li=[]
for i in range(n):
    num=int(input("enter the number"))
    li.append(num)


n1=int(input("enter the limit"))
li1=[]
for i in range(n1):
    num1=int(input("enter the number"))
    li1.append(num1)
print(li)
print(li1)

 # To check the list are of same length
a=len(li)
b=len(li1)
if a==b:
    print("The length of both list are same")
else:
    print("The length are not same")

#sum of list
sum=0
for i in li:
    sum=sum+i

sum1=0
for i in li1:
    sum1=sum1+i

if sum1==sum:
    print("sum of both the list are",sum)
else:
    print("The sum are not same")

#intersection
set2=set(li1)
set=set(li)


y=set2.intersection(set)
newli=list(y)
print("common elemrnts are",newli)

