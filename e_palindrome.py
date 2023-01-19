num=int(input("enter the number"))
copy=num
sum=0
for i in range(0,len(str(num))):
    rem=num%10
    sum=(sum*10)+rem
    num=num//10

if sum==copy:
    print("entered number is palindrome")
else:
    print("entered number is not palindrome")

