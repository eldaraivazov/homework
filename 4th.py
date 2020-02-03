from random import randint
a = int(input('Введіть довжину першого списку'))
b = int(input('Введіть максимальний елемент першого списку'))
c = []
for i in range (a):
    c.append(randint(0,b ))
print(c)
d = int(input('Введіть довжину другого списку'))
e = int(input('Введіть максимальний елемент другого списку'))
f = []
for i in range (d):
    f.append(randint(0,e ))
print(f)
result = list(set(c) & set(f))
print('І в нас співпали наступні числа: ' + str(result))
if(result==[]):
    print('Нажаль співпадіння відсутні')
