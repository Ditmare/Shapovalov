def obichn(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
def blizn(n):
    result = []
    for i in range(n, 2 * n - 1):
        if obichn(i) and obichn(i + 2):
            result.append((i, i + 2))

    return result

n = 125
result = blizn(n)
for i in result:
    print(i)