import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [random.randint(0, 100000) for _ in range(100000)]

print("50 primeiros elementos não ordenados:")
print(arr[:50])

start_time = time.time()
arr_ordenado = quick_sort(arr)
end_time = time.time()

print("\n50 primeiros elementos ordenados:")
print(arr_ordenado[:50])

print(f"\nTempo de execução: {end_time - start_time} segundos")
input("Pressione Enter para continuar...")