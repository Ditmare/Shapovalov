a = [1, 52, 2, 3248, 3843, 134231, 633]
def max(a):
    maximum = float('-10000000000000')

    for i in a:
        if i % 2 == 0 and i > maximum:
            maximum = i

    return maximum

maximum = max(a)
if maximum % 2 == 0:
    print("Наибольший элемент списка, который делится на 2 без остатка:", maximum)
else:
    print("В списке нет четных чисел.")