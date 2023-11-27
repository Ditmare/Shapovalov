matriza = []
with open('Шаповалов_У233_vvod.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matriza.append(row)
def obmen(matriza, i, j):
    for num in matriza:
        num[i], num[j] = num[j], num[i]
    return matriza

def minimal(matriza):
    n = len(matriza[0])
    minn = float('inf')
    min_i = 0
    for j in range(n):
        a = 1
        for i in range(len(matriza)):
            zn = matriza[i][j]
            if abs(zn) <= 10:
                a *= zn
            else:
                a = float('inf')
                break
        if a < minn:
            minn = a
            min_i = j

    if min_i > 0:
        matriza = obmen(matriza, min_i, min_i - 1)

    return matriza

itogmatriza = minimal(matriza)
itogmatriza_str = ' '.join(map(str, itogmatriza))

with open('Шаповалов_У-233_vivod.txt', 'w') as file:
    file.write(itogmatriza_str)
