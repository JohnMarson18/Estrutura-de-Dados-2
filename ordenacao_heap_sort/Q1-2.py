import random
import time
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

arr = [random.randint(0, 100000) for _ in range(100000)]

print("50 primeiros elementos não ordenados:")
print(arr[:50])

start_time = time.time()
arr_ordenado = heap_sort(arr)
end_time = time.time()

print("\n50 primeiros elementos ordenados:")
print(arr_ordenado[:50])

print(f"\nTempo de execução: {end_time - start_time} segundos")
input("Pressione Enter para continuar...")