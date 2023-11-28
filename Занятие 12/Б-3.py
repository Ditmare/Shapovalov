def nechet():
    n = int(input("Введите число: "))
    i = 1
    while n != 0:
        if i % 2 != 0:
            print(n)
        n = int(input("Введите число: "))
        i += 1

print(nechet())