def kvadr(N):
    num = 1
    sq = 1
    while sq <= N:
        print(sq)
        num += 1
        sq = num ** 2

N = int(input("Введите число N: "))
print("Квадраты натуральных чисел, не превосходящие", N, ":")
print(kvadr(N))
