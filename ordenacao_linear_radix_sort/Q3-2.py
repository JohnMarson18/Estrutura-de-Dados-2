import random
import time

def counting_sort(A, exp):
    n = len(A)
    B = [0] * n
    C = [0] * (k+1)

    for i in range(n):
        index = (A[i] // exp) % 10
        C[index] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        index = (A[i] // exp) % 10
        B[C[index] - 1] = A[i]
        C[index] -= 1

    for i in range(n):
        A[i] = B[i]


def radix_sort(A):

    exp = 1
    while k // exp > 0:
        counting_sort(A, exp)
        exp *= 10

print("\n-----------Radix Sort-------------")
n = 10**5

A = [random.randint(0, n) for _ in range(n)]
k = max(A)

print(f"\nValor máximo dos números(k): {k}\n")

print("-> Vetor original:\n ")
for i in range(n):
    print(f" {A[i]} /" , end=" ")


start_time = time.time()
radix_sort(A)
end_time = time.time()


print("\n\n-> Vetor ordenado:\n")
for i in range(n):
   print(f" {A[i]} /" , end=" ")

execution_time_ms = (end_time - start_time) * 1000
print(f"\n\nTempo de execução para ordenar {n} números: {execution_time_ms:.6f} milissegundos\n\n")
input("Pressione Enter para continuar...")
