class Node:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.valor = chave
        self.altura = 1 
        self.fator_balanceamento = 0 

class ArvoreAVL:
    def inserir(self, raiz, chave):
        if not raiz:
            return Node(chave)
        elif chave < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        else:
            raiz.direita = self.inserir(raiz.direita, chave)

        raiz.altura = 1 + max(self.obter_altura(raiz.esquerda), self.obter_altura(raiz.direita))
        raiz.fator_balanceamento = self.obter_balanceamento(raiz)
        return self.balancear_arvore(raiz)

    def obter_altura(self, Node):
        if not Node:
            return 0
        return Node.altura

    def obter_balanceamento(self, Node):
        if not Node:
            return 0
        return self.obter_altura(Node.esquerda) - self.obter_altura(Node.direita)

    def balancear_arvore(self, Node):
        # Caso 1: Rotação à direita
        if Node.fator_balanceamento > 1 and self.obter_balanceamento(Node.esquerda) >= 0:
            return self.rotacionar_direita(Node)
        # Caso 2: Rotação à esquerda
        if Node.fator_balanceamento < -1 and self.obter_balanceamento(Node.direita) <= 0:
            return self.rotacionar_esquerda(Node)
        # Caso 3: Rotação dupla à esquerda
        if Node.fator_balanceamento > 1 and self.obter_balanceamento(Node.esquerda) < 0:
            Node.esquerda = self.rotacionar_esquerda(Node.esquerda)
            return self.rotacionar_direita(Node)
        # Caso 4: Rotação dupla à direita
        if Node.fator_balanceamento < -1 and self.obter_balanceamento(Node.direita) > 0:
            Node.direita = self.rotacionar_direita(Node.direita)
            return self.rotacionar_esquerda(Node)
        return Node

    def rotacionar_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        z.fator_balanceamento = self.obter_balanceamento(z)
        y.fator_balanceamento = self.obter_balanceamento(y)
        return y

    def rotacionar_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        z.fator_balanceamento = self.obter_balanceamento(z)
        y.fator_balanceamento = self.obter_balanceamento(y)
        return y

    def imprimir_hierarquia(self, Node, nivel=0):
        if Node is not None:
            print("    " * nivel + f"Nível {nivel} ({Node.valor}) [{Node.fator_balanceamento}]")
            self.imprimir_hierarquia(Node.esquerda, nivel + 1)
            self.imprimir_hierarquia(Node.direita, nivel + 1)

arvore_avl = ArvoreAVL()
raiz = None

numeros = [40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75]

for numero in numeros:
    raiz = arvore_avl.inserir(raiz, numero)
    
arvore_avl.imprimir_hierarquia(raiz)
input("Pressione Enter para sair...")