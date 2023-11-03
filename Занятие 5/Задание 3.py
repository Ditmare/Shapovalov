N = int(input("Введите число N: "))
def bolsh(N):
    summ = 0
    result = 1
    while result <= N:
        summ += 1
        result *= 2
    return summ - 1, result // 2
summ, result = bolsh(N)
print('Наибольшая целая степень двойки, не превосходящая N, это 2^',summ, ' = ', result)
