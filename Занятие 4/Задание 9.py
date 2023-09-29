# -*- coding: utf-8 -*-
N = int(input('Введите число '))
fin1 = 1
fin2 = 1
g = 0
summ = 0
B = [1,1]
while summ < N-2:
    g = fin1 + fin2
    B.append(g)
    fin1 = fin2
    fin2 = g
    summ += 1
print(sum(B))