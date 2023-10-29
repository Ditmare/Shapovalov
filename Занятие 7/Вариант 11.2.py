a = [3, 8, 12, 4, 2, 5, 9, 4]
def mensh(a):
    result = []
    for i in a:
        if i % 2 == 0 and i < 10:
            result.append(i)

    if len(result) == 0:
        return "В исходном массиве нет четных чисел, меньших 10."

    result.sort()
    return result

result = mensh(a)
print(result)