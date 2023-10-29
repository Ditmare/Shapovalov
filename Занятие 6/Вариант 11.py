s = "нн!!!!!!!!!!ннннн..."
def stroka(s):
    max = 0
    a = 0
    for i in s:
        if i == 'н':
            a += 1
            if a > max:
                max = a
        else:
            a = 0

    izm_s = s.replace('!', '.')
    return izm_s, max

izm_s, count = stroka(s)
print("Результат:", izm_s)
print("Наибольшее количество 'н':", count)