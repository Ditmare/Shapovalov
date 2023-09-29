# -*- coding: utf-8 -*-
#Задача 10
N = int(input('Введите кол-во чисел Фибоначчи '))
K = int(input('Введите порядковый номер числа '))
fin1 = 1
fin2 = 1
g = 0
summ = 0
summ2 = 0
A = []
B = []
while summ2 < N:
    summ += 1
    if len(A) <= 1:
        A.append(1)
    else:
        g = fin1 + fin2
        fin1 = fin2
        fin2 = g
        A.append(g)
    if summ >= K:
        B.append(A[-1])
        summ2 += 1
print(sum(B))