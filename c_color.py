c1=input("enter the colors").split(',')
c2=input("enter the  second color").split(',')
set1=set(c1)
set2=set(c2)
y=set1.difference(set2)
print(y)
print(list(y))



# l=[i*i for i in range(5) if i<10]
# print(l)