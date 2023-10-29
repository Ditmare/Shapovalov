def max(matrix):
    max_value = matrix[0][0]
    max1 = 0
    max2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max1 = i
                max2 = j

    return max_value, max1, max2
def obmen(matrix1, matrix2):
    max_value1, max11, max21 = max(matrix1)
    max_value2, max12, max22 = max(matrix2)
    matrix1[max11][max21], matrix2[max12][max22] = matrix2[max12][max22], matrix1[max11][max21]

A = [[3, 5, 3],
     [2, 53, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 15, 4],
     [3, 2, 1]]
obmen(A, B)
print("Матрица A после обмена:")
for i in A:
    print(i)

print("Матрица B после обмена:")
for i in B:
    print(i)