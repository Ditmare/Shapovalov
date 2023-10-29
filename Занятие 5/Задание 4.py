def days(x, y):
    day = 1
    dist = x
    while dist < y:
        dist *= 1.1
        day += 1
    return day

x = float(input("Введите пробег в первый день (в километрах): "))
y = float(input("Введите целевой пробег (в километрах): "))
day = days(x, y)
print('Пробег спортсмена составит не менее', y,'километров на', day, 'день')