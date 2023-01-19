n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
gcd=0
if(n1>n2):
    i=1
    while(i<=n2):
        if(n1%i==0 and n2%i==0):
            gcd=i
        i=i+1
else:
    i = 1
    while (i <= n1):
        if (n1 % i == 0 and n2 % i == 0):
            gcd = i
        i = i + 1
print("gcd of %d and %d is"%(n1,n2),gcd)
