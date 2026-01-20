import random

# Gerar uma sequência aleatória de 50 números
numeros = random.sample(range(0, 100), 50)

class Nodo:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.valor = chave

# Funções da árvore ABB
def inserir_abb(raiz, chave):
    if raiz is None:
        return Nodo(chave)
    else:
        if raiz.valor < chave:
            raiz.direita = inserir_abb(raiz.direita, chave)
        else:
            raiz.esquerda = inserir_abb(raiz.esquerda, chave)
    return raiz

def em_ordem_abb(raiz):
    return em_ordem_abb(raiz.esquerda) + [raiz.valor] + em_ordem_abb(raiz.direita) if raiz else []

def pre_ordem_abb(raiz):
    return [raiz.valor] + pre_ordem_abb(raiz.esquerda) + pre_ordem_abb(raiz.direita) if raiz else []

def pos_ordem_abb(raiz):
    return pos_ordem_abb(raiz.esquerda) + pos_ordem_abb(raiz.direita) + [raiz.valor] if raiz else []

# Criar a árvore ABB
raiz_abb = None
for num in numeros:
    raiz_abb = inserir_abb(raiz_abb, num)

print("ABB Em-ordem:", em_ordem_abb(raiz_abb))
print("ABB Pré-ordem:", pre_ordem_abb(raiz_abb))
print("ABB Pós-ordem:", pos_ordem_abb(raiz_abb))

# Funções da árvore AVL
class NodoAVL:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.valor = chave
        self.altura = 1

def inserir_avl(raiz, chave):
    if not raiz:
        return NodoAVL(chave)
    elif chave < raiz.valor:
        raiz.esquerda = inserir_avl(raiz.esquerda, chave)
    else:
        raiz.direita = inserir_avl(raiz.direita, chave)

    raiz.altura = 1 + max(altura_avl(raiz.esquerda), altura_avl(raiz.direita))

    balance = obter_balance_avl(raiz)

    if balance > 1 and chave < raiz.esquerda.valor:
        return rotacao_direita_avl(raiz)

    if balance < -1 and chave > raiz.direita.valor:
        return rotacao_esquerda_avl(raiz)

    if balance > 1 and chave > raiz.esquerda.valor:
        raiz.esquerda = rotacao_esquerda_avl(raiz.esquerda)
        return rotacao_direita_avl(raiz)

    if balance < -1 and chave < raiz.direita.valor:
        raiz.direita = rotacao_direita_avl(raiz.direita)
        return rotacao_esquerda_avl(raiz)

    return raiz

def altura_avl(raiz):
    if not raiz:
        return 0
    return raiz.altura

def obter_balance_avl(raiz):
    if not raiz:
        return 0
    return altura_avl(raiz.esquerda) - altura_avl(raiz.direita)

def rotacao_esquerda_avl(z):
    y = z.direita
    T2 = y.esquerda

    y.esquerda = z
    z.direita = T2

    z.altura = 1 + max(altura_avl(z.esquerda), altura_avl(z.direita))
    y.altura = 1 + max(altura_avl(y.esquerda), altura_avl(y.direita))

    return y

def rotacao_direita_avl(z):
    y = z.esquerda
    T3 = y.direita

    y.direita = z
    z.esquerda = T3

    z.altura = 1 + max(altura_avl(z.esquerda), altura_avl(z.direita))
    y.altura = 1 + max(altura_avl(y.esquerda), altura_avl(y.direita))

    return y

def em_ordem_avl(raiz):
    return em_ordem_avl(raiz.esquerda) + [raiz.valor] + em_ordem_avl(raiz.direita) if raiz else []

def pre_ordem_avl(raiz):
    return [raiz.valor] + pre_ordem_avl(raiz.esquerda) + pre_ordem_avl(raiz.direita) if raiz else []

def pos_ordem_avl(raiz):
    return pos_ordem_avl(raiz.esquerda) + pos_ordem_avl(raiz.direita) + [raiz.valor] if raiz else []

# Criar a árvore AVL
raiz_avl = None
for num in numeros:
    raiz_avl = inserir_avl(raiz_avl, num)

print("AVL Em-ordem:", em_ordem_avl(raiz_avl))
print("AVL Pré-ordem:", pre_ordem_avl(raiz_avl))
print("AVL Pós-ordem:", pos_ordem_avl(raiz_avl))

# Comparar os percursos
abb_em_ordem = em_ordem_abb(raiz_abb)
avl_em_ordem = em_ordem_avl(raiz_avl)

abb_pre_ordem = pre_ordem_abb(raiz_abb)
avl_pre_ordem = pre_ordem_avl(raiz_avl)

abb_pos_ordem = pos_ordem_abb(raiz_abb)
avl_pos_ordem = pos_ordem_avl(raiz_avl)

print("Percursos Em-ordem são iguais?", abb_em_ordem == avl_em_ordem)
print("Percursos Pré-ordem são iguais?", abb_pre_ordem == avl_pre_ordem)
print("Percursos Pós-ordem são iguais?", abb_pos_ordem == avl_pos_ordem)
input("Pressione Enter para sair...")
