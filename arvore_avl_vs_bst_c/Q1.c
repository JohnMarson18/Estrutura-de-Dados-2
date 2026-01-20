#include <stdio.h>
#include <stdlib.h>

// Estrutura para os nós da árvore
typedef struct Node
{
    int key;
    struct Node *left, *right;
    int height; // Necessário para AVL
} Node;

// Função para criar um novo nó
Node *createNode(int key)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->key = key;
    node->left = node->right = NULL;
    node->height = 1; // Altura inicial para AVL
    return node;
}

// Função para obter a altura do nó (AVL)
int height(Node *node)
{
    return node ? node->height : 0;
}

// Função para calcular o fator de balanceamento (AVL)
int getBalance(Node *node)
{
    return node ? height(node->left) - height(node->right) : 0;
}

// Rotação à direita (AVL)
Node *rotateRight(Node *y)
{
    Node *x = y->left;
    Node *T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = 1 + (height(y->left) > height(y->right) ? height(y->left) : height(y->right));
    x->height = 1 + (height(x->left) > height(x->right) ? height(x->left) : height(x->right));

    return x;
}

// Rotação à esquerda (AVL)
Node *rotateLeft(Node *x)
{
    Node *y = x->right;
    Node *T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = 1 + (height(x->left) > height(x->right) ? height(x->left) : height(x->right));
    y->height = 1 + (height(y->left) > height(y->right) ? height(y->left) : height(y->right));

    return y;
}

// Inserção na Árvore Binária de Busca (BST)
Node *insertBST(Node *node, int key)
{
    if (!node)
        return createNode(key);
    if (key < node->key)
        node->left = insertBST(node->left, key);
    else if (key > node->key)
        node->right = insertBST(node->right, key);
    return node;
}

// Inserção na Árvore AVL
Node *insertAVL(Node *node, int key)
{
    if (!node)
        return createNode(key);
    if (key < node->key)
        node->left = insertAVL(node->left, key);
    else if (key > node->key)
        node->right = insertAVL(node->right, key);
    else
        return node; // Chaves duplicadas não são permitidas

    node->height = 1 + (height(node->left) > height(node->right) ? height(node->left) : height(node->right));

    int balance = getBalance(node);

    // Rotação LL
    if (balance > 1 && key < node->left->key)
        return rotateRight(node);

    // Rotação RR
    if (balance < -1 && key > node->right->key)
        return rotateLeft(node);

    // Rotação LR
    if (balance > 1 && key > node->left->key)
    {
        node->left = rotateLeft(node->left);
        return rotateRight(node);
    }

    // Rotação RL
    if (balance < -1 && key < node->right->key)
    {
        node->right = rotateRight(node->right);
        return rotateLeft(node);
    }

    return node;
}

// Função para calcular a altura da árvore
int calculateHeight(Node *node)
{
    if (!node)
        return 0;
    int leftHeight = calculateHeight(node->left);
    int rightHeight = calculateHeight(node->right);
    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

// Função principal
int main()
{
    Node *bstRoot = NULL; // Raiz da BST
    Node *avlRoot = NULL; // Raiz da AVL

    int n = 10000; // Quantidade de números a serem inseridos
    int randomNumbers[n];

    // Gerar números aleatórios
    for (int i = 0; i < n; i++)
    {
        randomNumbers[i] = rand() % 100000; // Números entre 0 e 99999
    }

    // Inserir números na BST e na AVL
    for (int i = 0; i < n; i++)
    {
        bstRoot = insertBST(bstRoot, randomNumbers[i]);
        avlRoot = insertAVL(avlRoot, randomNumbers[i]);
    }

    // Calcular alturas
    int bstHeight = calculateHeight(bstRoot);
    int avlHeight = calculateHeight(avlRoot);

    // Mostrar resultados
    printf("Altura da Arvore Binaria de Busca (BST): %d\n", bstHeight);
    printf("Altura da Arvore AVL: %d\n", avlHeight);
    
    printf("Pressione Enter para sair..."); 
    getchar();
    return 0;
}
