n = int(input('Введите число: '))
def prostoe(n):
    if n <= 1:
        return "NO"
    elif n <= 3:
        return "YES"
    elif n % 2 == 0 or n % 3 == 0:
        return "NO"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "NO"
        i += 6
    return "YES"


print(prostoe(n))