
# limit=int(input("enter the limit"))
# print("The leap years are:")
# for i in range(2022,limit+1):
#     if i%4==0 :
#         print(i,"\n")

n = input("Please enter year")

year = int(n)

if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print("%d is a Leap Year" % year)
else:
    print("%d is Not the Leap Year" % year)