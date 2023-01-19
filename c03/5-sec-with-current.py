import datetime
x= datetime.datetime.now()
print(x)
y = x + datetime.timedelta(0,5)
print(x.time())
print(y.time())
