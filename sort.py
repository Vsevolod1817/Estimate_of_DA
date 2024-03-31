import random

def create_random_array(size):
    return [random.randint(0, 100) for _ in range(size)]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Генерируем случайный массив
size = 10
array = create_random_array(size)

# Выводим исходный массив
print("Исходный массив:", array)

# Сортировка массива методом вставки
insertion_sorted_array = array.copy()
insertion_sort(insertion_sorted_array)
print("Отсортированный массив (вставкой):", insertion_sorted_array)

# Сортировка массива методом выбора
selection_sorted_array = array.copy()
selection_sort(selection_sorted_array)
print("Отсортированный массив (выбором):", selection_sorted_array)

# Сортировка массива методом пузырька
bubble_sorted_array = array.copy()
bubble_sort(bubble_sorted_array)
print("Отсортированный массив (пузырьком):", bubble_sorted_array)
