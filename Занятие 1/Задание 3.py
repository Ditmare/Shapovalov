# -*- coding: utf-8 -*-
#Задача 3
name = input('Введите ваше имя ')
age = int(input('Введите ваш возраст '))
if name == 'Иван' or name == 'иван':
    print('Поменяйте ваше имя, Иван')
if age < 0 or age > 75:
    print('Скорее всего вы неверно ввели возраст, запустите заново')
if age < 16:
    print('Вам ещё учиться:', 16 - age, 'лет')
if age >= 16 and age >0 and age < 75 and name != 'Иван':
    print('Поздравляю вы поступили в ВГУИТ')