import random

def create_random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(0, 9))  # Генерируем случайное целое число от 0 до 9
        matrix.append(row)
    return matrix

def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None  # Возвращаем None, если размерности матриц не совпадают для умножения

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Генерация случайных матриц
rows1 = 3
cols1 = 3
matrix1 = create_random_matrix(rows1, cols1)

rows2 = 3
cols2 = 3
matrix2 = create_random_matrix(rows2, cols2)

# Вывод матриц
print("Первая матрица:")
for row in matrix1:
    print(row)

print("Вторая матрица:")
for row in matrix2:
    print(row)

# Умножение матриц
result = matrix_multiply(matrix1, matrix2)

if result is not None:
    print("Результат перемножения матриц:")
    for row in result:
        print(row)
else:
    print("Невозможно перемножить данные матрицы")
