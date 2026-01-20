# 📚 Estruturas de Dados Avançadas e Algoritmos de Ordenação

Este repositório reúne a resolução completa de exercícios práticos da disciplina de **Estrutura de Dados II**.
O projeto abrange desde a implementação de **Filas de Prioridade** e algoritmos de **Ordenação Eficiente**, até estruturas complexas de árvores (**AVL, Rubro-Negra, B**) e algoritmos de caminho mínimo em **Grafos**.

O código foi desenvolvido em **Python** e **C**, com foco em análise de complexidade, manipulação de ponteiros e comparação de desempenho.

## 👨‍💻 Autores
* **Paulo Fernando Pereira Junior**
* **Maria Luiza Souza da Silva**

## 🎓 Orientação Acadêmica
* **Disciplina:** Estrutura de Dados II

---

## 📂 Estrutura do Projeto

O repositório está organizado por tópicos. Abaixo, o detalhamento de cada implementação:

### ⚡ 1. Estrutura de Fila de Prioridade (Heap)
Implementação de um sistema de gerenciamento de processos utilizando *Min-Heap*.

| Arquivo | Descrição | Destaques Técnicos |
| :--- | :--- | :--- |
| `Q2.py` | Gerenciador de processos com prioridade. | Uso da biblioteca `heapq` para operações de heap. Implementação de operador de comparação `__lt__` na classe `Processo` para desempate por ordem de chegada. |

### ⏱️ 2. Algoritmos de Ordenação (Sorting)
Implementação e análise de tempo de algoritmos $O(n \log n)$ e lineares.

#### 🔢 Ordenação por Comparação
| Arquivo | Algoritmo | Análise Técnica |
| :--- | :--- | :--- |
| `Q1-2.py` | **Heap Sort** | Transforma a lista em heap e extrai elementos sucessivamente via *list comprehension*. |
| `Q1-3.py` | **Merge Sort** | Divisão recursiva do vetor e conquista na função `merge`. Intercalação de sub-listas ordenadas. |
| `Q1-4.py` | **Quick Sort** | Implementação "Pythonic" recursiva particionando em listas *left*, *middle* e *right*. |
| `Q1-1.py` | **Shell Sort** | Ordenação por inserção com diminuição gradual do intervalo (`gap`) até chegar a 0. |

#### 📊 Ordenação Linear
| Arquivo | Algoritmo | Análise Técnica |
| :--- | :--- | :--- |
| `Q3-3.py` | **Bucket Sort** | Distribuição baseada em `bucket_size` seguida de `insertion_sort` dentro de cada balde. |
| `Q3-1.py` | **Counting Sort** | Criação de vetor de contagem `C` baseado no valor máximo `k` e reconstrução do vetor ordenado `B`. |
| `Q3-2.py` | **Radix Sort** | Ordenação dígito a dígito (LSD - Least Significant Digit) reutilizando a lógica do Counting Sort para cada expoente. |

### 🌲 3. Árvores Balanceadas (AVL e BST)
Estudos comparativos entre Árvores Binárias de Busca (BST) simples e Árvores AVL (Auto-balanceáveis).

| Diretório/Arquivo | Descrição | Destaques Técnicos |
| :--- | :--- | :--- |
| `Q1.c` | **Comparativo BST vs AVL (C)** | Implementação de rotações (`rotateRight`, `rotateLeft`). Cálculo explícito de altura para verificação de balanceamento e inserção recursiva. |
| `Q2/Q2.py` | **Percursos em Árvores (Python)** | Comparação de percursos Em-ordem, Pré-ordem e Pós-ordem. Implementação de rotações duplas (LR, RL) na inserção AVL. |
| `Q3/Q3.py` | **Hierarquia AVL** | Classe com atributo `fator_balanceamento`. Visualização hierárquica dos nós por nível (ex: `Nível 0`, `Nível 1`). |

### 🍁 4. Árvores Complexas (Rubro-Negra e B)
Implementações avançadas em C para estruturas de alta performance.

| Arquivo | Descrição | Destaques Técnicos |
| :--- | :--- | :--- |
| `Q4.c` | **Rubro-Negra vs Árvore B** | **Rubro-Negra:** Nós com propriedade de cor (`RED`/`BLACK`) e função `trocaCor`. **Árvore B:** Estrutura de nós preparada para divisão e inserção de chaves. |

### 🌐 5. Algoritmos em Grafos
Implementação de caminhos mínimos utilizando C.

| Arquivo | Algoritmo | Destaques Técnicos |
| :--- | :--- | :--- |
| `Q5.c` | **Dijkstra** | Grafo representado por lista de adjacência dinâmica com `realloc`. Uso de vetor `dist` e `visitado` para relaxamento de arestas e busca do menor caminho. |

---

## 🚀 Como Executar

### Pré-requisitos
* Compilador **GCC** para os códigos em C.
* Interpretador **Python 3.x** para os scripts `.py`.

### Exemplos de Execução

**1. Executando o Heap Sort (Python):**
```bash
python ordenacao_heap_sort/Q1-2.py
