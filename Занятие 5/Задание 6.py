def sredn():
    count = 0
    kon = 0
    while True:
        n = int(input("Введите число (или 0 для завершения): "))
        if n == 0:
            break
        count += 1
        kon += n
    if count == 0:
        return 0
    else:
        return kon / count

otvet = sredn()
print('Среднее значение всех элементов последовательности:', otvet)