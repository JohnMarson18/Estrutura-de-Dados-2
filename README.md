📚 Estruturas de Dados Avançadas e Algoritmos de Ordenação

Este repositório reúne a resolução completa de exercícios práticos da disciplina de Estrutura de Dados II (ED2). O projeto abrange desde a implementação de Filas de Prioridade e algoritmos de Ordenação Eficiente, até estruturas complexas de árvores (AVL, Rubro-Negra, B) e algoritmos em Grafos.

O código foi desenvolvido em Python e C, com foco em análise de complexidade, manipulação de ponteiros e comparação de desempenho.
👨‍💻 Autores

    Paulo Fernando Pereira Junior

    Maria Luiza Souza

🎓 Orientação Acadêmica

    Disciplina: Estrutura de Dados II

📂 Estrutura do Projeto

O repositório está organizado por tópicos. Abaixo, o detalhamento de cada implementação:
⚡ 1. Estrutura de Fila de Prioridade (Heap)

Implementação de um sistema de gerenciamento de processos utilizando Min-Heap. | Arquivo | Descrição | Destaques Técnicos | | :--- | :--- | :--- | | Q2.py | Gerenciador de processos com prioridade. | Uso da biblioteca heapq para manter a propriedade de heap min. Implementação de operador de comparação __lt__ para desempate por ordem de chegada. |

⏱️ 2. Algoritmos de Ordenação (Sorting)

Implementação e análise de tempo de algoritmos O(nlogn) e lineares.
🔢 Ordenação por Comparação
Arquivo	Algoritmo	Análise Técnica
Q1-2.py	Heap Sort	

Transforma a lista em heap e extrai elementos sucessivamente.

Q1-3.py	Merge Sort	

Divisão recursiva do vetor e conquista na função merge. Intercalação de sub-listas ordenadas.

Q1-4.py	Quick Sort	

Implementação "Pythonic" usando list comprehension para particionar pivôs.

Q1-1.py	Shell Sort	

Ordenação por inserção com diminuição gradual do intervalo (gap).

📊 Ordenação Linear
Arquivo	Algoritmo	Análise Técnica
Q3-3.py	Bucket Sort	

Distribuição em baldes seguida de insertion_sort em cada balde. Concatenação final dos buckets.

Q3-1.py	Counting Sort	

Criação de vetor de contagem C baseado no valor máximo k. Reconstrução do vetor ordenado via contagem cumulativa.

Q3-2.py	Radix Sort	

Ordenação dígito a dígito (LSD) reutilizando a lógica do Counting Sort para cada expoente.

🌲 3. Árvores Balanceadas (AVL e BST)

Estudos comparativos entre Árvores Binárias de Busca (BST) simples e Árvores AVL (Auto-balanceáveis).
Diretório/Arquivo	Descrição	Destaques Técnicos
Q1.c	Comparativo BST vs AVL (C)	

Implementação de rotações à direitae à esquerda. Cálculo explícito de altura e fator de balanceamento. Comparação final de altura entre as duas estruturas.

Q2/Q2.py	Percursos em Árvores (Python)	

Comparação de percursos Em-ordem, Pré-ordem e Pós-ordem entre ABB e AVL. Atualização de altura dinâmica na inserção.

Q3/Q3.py	Hierarquia AVL	

Visualização hierárquica dos nós e seus fatores de balanceamento. Tratamento dos 4 casos de rotação (Simples e Dupla).

🍁 4. Árvores Complexas (Rubro-Negra e B)

Implementações avançadas em C para estruturas de alta performance.
Arquivo	Descrição	Destaques Técnicos
Q4.c	Rubro-Negra vs Árvore B	

Definição de nós com propriedade de cor (RED/BLACK). Rotações específicas com troca de cores. Inserção com correção automática de violações rubro-negras.

🌐 5. Algoritmos em Grafos

Implementação de caminhos mínimos.
Arquivo	Algoritmo	Destaques Técnicos
Q5.c	Dijkstra	

Grafo representado por lista de adjacência (Grafo struct). Função procuraMenorDistancia para escolher o próximo vértice. Relaxamento de arestas para atualizar distâncias.

🚀 Como Executar
Códigos em Python

Certifique-se de ter o Python instalado. Exemplo de execução do Heap Sort:
Bash

python Q1-2.py

Códigos em C

Para compilar os projetos em C (ex: AVL), utilize o GCC:
Bash

gcc Q1.c -o arvore_avl
./arvore_avl
