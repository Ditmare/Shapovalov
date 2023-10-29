def count_el():
    count = -1
    num = 0
    while True:
        n = int(input("Введите число (или 0 для завершения): "))
        if n == 0:
            break
        if n > num:
            count += 1
        n = num
    return count

count = count_el()
print('Количество элементов последовательности, больших предыдущего элемента:', count)