# -*- coding: utf-8 -*-
#Задача 1
A = int(input('Введите A, меньше чем B '))
B = int(input('Введите B '))
if A<=B:
    for i in range(A,B+1):
        print(i,end=' ')
else:
    print('A меньше B')