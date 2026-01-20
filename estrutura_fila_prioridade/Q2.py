import heapq
import random

class Processo:
    def __init__(self, prioridade, ordem_chegada, valor):
        self.prioridade = prioridade
        self.ordem_chegada = ordem_chegada
        self.valor = valor

    def __lt__(self, outro):
        if self.prioridade == outro.prioridade:
            if self.ordem_chegada == outro.ordem_chegada:
                return self.valor < outro.valor
            return self.ordem_chegada > outro.ordem_chegada
        return self.prioridade > outro.prioridade

    def __repr__(self):
        return f"Prioridade {self.prioridade}, Ordem de chegada {self.ordem_chegada}, Valor {self.valor}"

class FilaPrioridade:
    def __init__(self):
        self.heap = []

    def inserir_processo(self, prioridade, ordem_chegada):
        valor = random.randint(1, 10000)  # Gera um número aleatório entre 1 e 100
        processo = Processo(prioridade, ordem_chegada, valor)
        heapq.heappush(self.heap, processo)

    def deletar_processo(self):
        if not self.heap:
            print("Fila vazia")
            return
        processo = heapq.heappop(self.heap)
        print(f"Processo deletado: {processo}")

    def contar_processos(self):
        print(f"Quantidade de processos: {len(self.heap)}")

    def ver_processo_mais_prioritario(self):
        if not self.heap:
            print("Fila vazia")
            return
        processo = self.heap[0]
        print(f"Processo mais prioritário: {processo}")

    def imprimir_todos_processos(self):
        if not self.heap:
            print("Fila vazia")
            return
        print("Todos os processos:")
        for processo in self.heap:
            print(processo)

def main():
    fila = FilaPrioridade()
    ordem_chegada = 1

    while True:
        print("\nOpções:")
        print("1. Inserir processo")
        print("2. Deletar processo")
        print("3. Contar processos")
        print("4. Ver processo mais prioritário")
        print("5. Imprimir todos os processos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            prioridade = int(input("Digite a prioridade do processo: "))
            fila.inserir_processo(prioridade, ordem_chegada)
            ordem_chegada += 1
        elif opcao == "2":
            fila.deletar_processo()
        elif opcao == "3":
            fila.contar_processos()
        elif opcao == "4":
            fila.ver_processo_mais_prioritario()
        elif opcao == "5":
            fila.imprimir_todos_processos()
        elif opcao == "6":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()