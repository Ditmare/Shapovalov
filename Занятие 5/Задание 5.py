def kolvo():
    count = 0
    while True:
        num = int(input("Введите число (или 0 для завершения): "))
        if num == 0:
            break
        count += 1
    return count

count = kolvo()
print('Количество членов последовательности (не считая завершающего числа 0):',count)