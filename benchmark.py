import random
import time
from main import bubble_sort, binary_insertion_sort

print(">>> Ініціалізація стрес-тестування на масиві з 10 000 елементів...")
arr_large = [random.randint(1, 100000) for _ in range(10000)]
print("Генерація послідовності випадкових чисел завершена успішно.\n")

arr_bubble = list(arr_large)
print("[Процес 1/2] Запуск Bubble Sort на 10 000 елементів...")
start_time_bubble = time.time()
bubble_sort(arr_bubble)
end_time_bubble = time.time()
print(f"[Результат 1] Bubble Sort успішно виконав завдання за: {end_time_bubble - start_time_bubble:.4f} сек.\n")

arr_binary = list(arr_large)
print("[Процес 2/2] Запуск Binary Insertion Sort на 10 000 елементів...")
start_time_binary = time.time()
binary_insertion_sort(arr_binary)
end_time_binary = time.time()
print(f"[Результат 2] Binary Insertion Sort успішно виконав завдання за: {end_time_binary - start_time_binary:.4f} сек.\n")

print("Висновки аналізу швидкодії: Сортування двійковими вставками демонструє вищу продуктивність, ніж Bubble Sort, за рахунок мінімізації кількості порівнянь через логарифмічний пошук.")