# -*- coding: utf-8 -*-
#Задача 7
def vis(a):
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
        return True
    else:
        return False
a = int(input("Введите год: "))
if vis(a):
    print(a, "Да")
else:
    print(a, "Нет")