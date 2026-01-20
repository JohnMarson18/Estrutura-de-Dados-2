import random
import time


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(A, bucket_size=10):
    max_val = max(A)
    bucket_count = (max_val // bucket_size) + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in A:
        index = num // bucket_size
        buckets[index].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


print("\n---------------Bucket Sort------------------")

n = 10**5

A = [random.randint(0, n) for _ in range(n)]
k= max(A)
print(f"\nValor máximo dos números(k): {k}\n")

print("-> Vetor original:\n ")
for i in range(n):
    print(f" {A[i]} /" , end=" ")

start_time = time.time()
sorted_A = bucket_sort(A)
end_time = time.time()

print("\n\n-> Vetor ordenado: \n")
for i in range(n):
    print(f" {sorted_A[i]} /" , end=" ")

execution_time_ms = (end_time - start_time) * 1000
print(f"\n\nTempo de execução para ordenar {n} números: {execution_time_ms:.6f} milissegundos\n\n")
input("Pressione Enter para continuar...")

