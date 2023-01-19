n=int(input("enter the limit"))
for i in range(n):
    m=int(input("enter the number"))
oddsum=0
evensum=0

i=1;
while(i<=m):
    if i%2!=0:
        oddsum=oddsum+i
    else:
        evensum=evensum+i
    i=i+1
print("sum of odd number",oddsum)
print("sum of even number",evensum)

