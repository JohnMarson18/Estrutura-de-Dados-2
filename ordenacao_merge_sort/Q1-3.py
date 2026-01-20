import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = [0] * (len(left) + len(right))
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1
    return result

arr = [random.randint(0, 100000) for _ in range(100000)]

print("50 primeiros elementos não ordenados:")
print(arr[:50])

start_time = time.time()
arr_ordenado = merge_sort(arr)
end_time = time.time()

print("\n50 primeiros elementos ordenados:")
print(arr_ordenado[:50])

print(f"\nTempo de execução: {end_time - start_time} segundos")
input("Pressione Enter para continuar...")