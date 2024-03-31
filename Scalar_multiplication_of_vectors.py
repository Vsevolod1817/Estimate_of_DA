import random

def create_random_vector(size):
    vector = []
    for _ in range(size):
        vector.append(random.randint(0, 9))  # Генерируем случайное целое число от 0 до 9
    return vector

def scalar(vector1, vector2, m):
    for i in range(len(vector1)):
        m += vector1[i] * vector2[i]
    return m

# Создаем случайные векторы
size = 3
vector1 = create_random_vector(size)
vector2 = create_random_vector(size)
m = 0

# Выводим векторы
print("Первый вектор:", vector1)
print("Второй вектор:", vector2)

# Вычисляем скалярное произведение
print("Результат:", scalar(vector1, vector2, m))
