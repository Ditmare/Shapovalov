m = int(input("Введите порядок квадратной матрицы: "))
def matr(n):
    mat = []
    for i in range(n):
        a = []
        for j in range(n):
            num = float(input(f"Введите элемент [{i + 1}, {j + 1}]: "))
            a.append(num)
        mat.append(a)
    return mat

def summa(matriza):
    minn = matriza[0][0]
    min_zn = 0
    for i, num in enumerate(matriza):
        if min(num) < minn:
            minn = minn(num)
            min_zn = i
    min_zn = sum(matriza[min_zn])
    return min_zn

matriza = matr(m)
itog = summa(matriza)
print("Сумма элементов строки:", itog)