# -*- coding: utf-8 -*-
#Задача 5
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
def minn(x,y,z):
    if x < y and x < z:
        return(x)
    if y < x and y < z:
        return(y)
    if z < x and z < y:
        return(z)
print(minn(x,y,z))