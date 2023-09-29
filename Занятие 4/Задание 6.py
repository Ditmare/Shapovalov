# -*- coding: utf-8 -*-
#Задача 6
N = int(input('Введите число, факториал которого хотите увидеть '))
fak = 1
for i in range(1, N+1):
    fak *= i
print(fak)