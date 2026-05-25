import random
import time


# --- 1. Алгоритм Bubble Sort ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# --- 2. Алгоритм Binary Insertion Sort ---
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if val < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = val
    return arr


# --- 3. Виконання (Генерація 20 чисел) ---
if __name__ == "__main__":
    print("=== Bubble Sort (20 елементів) ===")
    arr1 = [random.randint(1, 100) for _ in range(20)]
    print(f"До сортування:    {arr1}")
    print(f"Після сортування: {bubble_sort(arr1.copy())}\n")

    print("=== Binary Insertion Sort (20 елементів) ===")
    arr2 = [random.randint(1, 100) for _ in range(20)]
    print(f"До сортування:    {arr2}")
    print(f"Після сортування: {binary_insertion_sort(arr2.copy())}\n")

    # --- 4. Замір часу (10 000 чисел) ---
    print("Генерація 10 000 випадкових чисел...")
    arr_large = [random.randint(1, 100000) for _ in range(10000)]

    start_time = time.time()
    binary_insertion_sort(arr_large.copy())
    print(f"Час Binary Sort: {time.time() - start_time:.4f} секунд")

    start_time = time.time()
    bubble_sort(arr_large.copy())
    print(f"Час Bubble Sort: {time.time() - start_time:.4f} секунд")