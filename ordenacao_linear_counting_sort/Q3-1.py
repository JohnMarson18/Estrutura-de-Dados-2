import random
import time
#A = [0, 2, 1, 0, 3, 1]

n = 10**5
A = [random.randint(0, n) for _ in range(n)]
k = max(A)  


B = [0] * n  
C = [0] * (k + 1)

print("\n-------Counting Sort--------")

print(f"\nValor máximo dos números(k): {k}\n")

print("-> Vetor original:\n ")
for i in range(n):
    print(f" {A[i]} /" , end=" ")
 
print("\n")

start_time = time.time()

for i in range(k + 1):
    C[i] = 0

for j in range(n):
    C[A[j]] += 1

for i in range(1, k + 1):
    C[i] += C[i - 1]

for i in range(n - 1, -1, -1):
    B[C[A[i]] - 1] = A[i]
    C[A[i]] -= 1

end_time = time.time()

print("\n\n-> Vetor ordenado:\n")
for i in range(n):
    print(f" {B[i]} /" , end=" ")

execution_time_ms = (end_time - start_time) * 1000
print(f"\n\nTempo de execução para ordenar {n} números: {execution_time_ms:.6f} milissegundos\n\n")
input("Pressione Enter para continuar...")


