n=int(input("enter the limit"))
i=0
while(i<=n):
    j=0
    while(j<i):
        print("*", end=" ")
        j=j+1

    print("\n")
    i=i+1

i=n-1
while(i>=0):
    j=0
    while(j<i):
        print("*", end=" ")
        j=j+1

    print("\n")
    i=i-1