# -*- coding: utf-8 -*-
#Задача 9
n = int(input('Введите число долек n '))
m = int(input('Введите число долек m '))
k = int(input('Введите число k '))
def rovn(n,m,k):
    if k < n*m and ((k%n == 0) or (k%m == 0)):
        return 'Да'
    else:
        return 'Нет'
print(rovn(n,m,k))