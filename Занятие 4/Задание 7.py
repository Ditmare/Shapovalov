# -*- coding: utf-8 -*-
#Задача 7
N = int(input('Введите число '))
fak = 1
sum_fak = 0
for i in range(1, N + 1):
    fak *= i
    sum_fak += fak
print(sum_fak)