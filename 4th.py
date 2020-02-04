from random import randint
a = int(input('Введіть довжину першого списку  '))
b = int(input('Введіть максимальний елемент першого списку  '))
c = int(input('Введіть довжину другого списку  '))
d = int(input('Введіть максимальний елемент другого списку  '))
def func (e,f,g,h):
    first = []
    for i in range(e):
        first.append(randint(0, f+1))


    second = []
    for i in range(g):
        second.append(randint(0, h+1))


    final = []
    for g in first:
        if g in second:
            final.append(g)

    if len(final) ==0:
        print('Співпадіння не виявлені')
        return final
    else:
        return list(set(final))
print (func(a,b,c,d))