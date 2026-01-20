import random
import time

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

arr = [random.randint(0, 100000) for _ in range(100000)]

print("50 primeiros elementos não ordenados:")
print(arr[:50])

start_time = time.time()
arr_ordenado = shell_sort(arr)
end_time = time.time()

print("\n50 primeiros elementos ordenados:")
print(arr_ordenado[:50])

print(f"\nTempo de execução: {end_time - start_time} segundos")
input("Pressione Enter para continuar...")