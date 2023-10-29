def small(n):
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor

n = int(input("Введите целое число (не меньше 2): "))
delit = small(n)
print('Наименьший натуральный делитель числа', n, 'отличный от 1, это', delit)