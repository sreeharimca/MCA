import random
import string
print("generate a random color hex ")
print('#{:06x}'.format(random.randint(0,0XFFFFFF)))
print("Generate a random alphabetic string")
max_length=255
s=""
for i in range(random.randint(1,max_length)):
    s+=random.choice(string.ascii_letters)
print(s)
print(random.randint(0,10))
print(random.randint(-7,7))
print(random.randint(1,1))
print("Generate random multiple of 7 between 0 and 70")
print(random.randint(0,10)*7)
