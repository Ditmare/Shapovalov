# -*- coding: utf-8 -*-
#Задача 3
A = int(input('Введите A '))
B = int(input('Введите B '))
if A>B:
    for i in range(A - (A + 1) % 2, B - B % 2, -2):
        print(i, end=' ')
else:
    print('A меньше чем B')