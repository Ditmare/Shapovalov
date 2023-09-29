#Задача 8
n = int(input('Введите число <= 9 '))
if n <= 9:
    for i in range(1, n + 1):
        for t in range(1, i + 1):
           print(t, end='')
        print()
else:
    print('n больше 9')