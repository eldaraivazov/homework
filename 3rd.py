from random import randint as zbs
a = zbs(0,11)
b = zbs(0,11)
c = zbs(0,11)
if a > b:
    print('Dont worry, be happy!')
elif a < b:
    print('Shit happens(')
elif a == b:
    print(c,'Теперь эта')
    if c > (a+b):
        print('Awesome')
    elif c < (a+b):
        print('sucks')
    elif c == (a+b):
        print ('Страдания')