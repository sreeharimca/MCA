f=int(input("enter the number"))
n=0
i=2
while(i<f):
    if f%i==0:
        n=1
        break;
    i+=1
if n==0:
    print("prime number")
else:
    print("not prime")

