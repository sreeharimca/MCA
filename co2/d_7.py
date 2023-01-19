str=input("enter the string")
revend=str[-1:-4:-1]
end=revend[::-1]

if end=="ing":
    print(str+'ly')
else:
    print(str+'ing')

