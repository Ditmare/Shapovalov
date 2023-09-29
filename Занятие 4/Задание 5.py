# -*- coding: utf-8 -*-
#Задача 5
N = int(input('Введите число '))
sum = 0
for i in range(1, N+1):
    sum += i**3
print(sum)