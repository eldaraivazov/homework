from random import randint

a = int(input('Введіть бажану довжину списку   '))
b = int(input('Введіть максимальне значення елементу списка   '))


def funky (c,d):
    list = []
    for i in range(c):
        list.append(randint(0, d + 1))
    return list


print(funky(a, b))
