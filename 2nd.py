from random import randint
a = 10
list = []
for i in range (a):
    list.append(randint(0,100))
print(list)
del list[-1]
print(list)