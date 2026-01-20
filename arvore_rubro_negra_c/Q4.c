#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define RED 0
#define BLACK 1

struct NO_RN
{
    int info;
    struct NO_RN *esq;
    struct NO_RN *dir;
    int cor;
};

struct NO_B
{
    int info;
    struct NO_B *esq;
    struct NO_B *dir;
};

typedef struct NO_RN *ArvRN;
typedef struct NO_B *ArvB;

int cor(struct NO_RN *H)
{
    if (H == NULL)
        return BLACK;
    else
        return H->cor;
}

ArvRN rotacionaEsquerda_RN(ArvRN h)
{
    ArvRN x = h->dir;
    h->dir = x->esq;
    x->esq = h;
    x->cor = h->cor;
    h->cor = RED;
    return x;
}

ArvRN rotacionaDireita_RN(ArvRN h)
{
    ArvRN x = h->esq;
    h->esq = x->dir;
    x->dir = h;
    x->cor = h->cor;
    h->cor = RED;
    return x;
}

void trocaCor_RN(ArvRN h)
{
    h->cor = !h->cor;
    if (h->esq != NULL)
        h->esq->cor = !h->esq->cor;
    if (h->dir != NULL)
        h->dir->cor = !h->dir->cor;
}

ArvRN insereNO_RN(ArvRN h, int valor, int *resp)
{
    if (h == NULL)
    {
        ArvRN novo = (ArvRN)malloc(sizeof(struct NO_RN));
        if (novo == NULL)
        {
            *resp = 0;
            return NULL;
        }
        novo->info = valor;
        novo->cor = RED;
        novo->dir = NULL;
        novo->esq = NULL;
        *resp = 1;
        return novo;
    }

    if (valor == h->info)
        *resp = 0;
    else
    {
        if (valor < h->info)
            h->esq = insereNO_RN(h->esq, valor, resp);
        else
            h->dir = insereNO_RN(h->dir, valor, resp);
    }

    if (cor(h->dir) == RED && cor(h->esq) == BLACK)
        h = rotacionaEsquerda_RN(h);
    if (cor(h->esq) == RED && cor(h->esq->esq) == RED)
        h = rotacionaDireita_RN(h);
    if (cor(h->esq) == RED && cor(h->dir) == RED)
        trocaCor_RN(h);

    return h;
}

ArvRN insere_RubroNegra(ArvRN h, int valor)
{
    int resp;
    h = insereNO_RN(h, valor, &resp);
    if (h != NULL)
        h->cor = BLACK;
    return h;
}

int alturaArvore_RN(ArvRN h)
{
    if (h == NULL)
        return 0;
    int alturaEsq = alturaArvore_RN(h->esq);
    int alturaDir = alturaArvore_RN(h->dir);
    return (alturaEsq > alturaDir ? alturaEsq : alturaDir) + 1;
}

ArvB rotacionaEsquerda_B(ArvB h)
{
    ArvB x = h->dir;
    h->dir = x->esq;
    x->esq = h;
    return x;
}

ArvB rotacionaDireita_B(ArvB h)
{
    ArvB x = h->esq;
    h->esq = x->dir;
    x->dir = h;
    return x;
}

ArvB insereNO_B(ArvB h, int valor)
{
    if (h == NULL)
    {
        ArvB novo = (ArvB)malloc(sizeof(struct NO_B));
        if (novo == NULL)
        {
            return NULL;
        }
        novo->info = valor;
        novo->dir = NULL;
        novo->esq = NULL;
        return novo;
    }

    if (valor < h->info)
        h->esq = insereNO_B(h->esq, valor);
    else
        h->dir = insereNO_B(h->dir, valor);

    if (h->dir != NULL && (h->esq == NULL || h->dir->info < h->esq->info))
        h = rotacionaEsquerda_B(h);
    if (h->esq != NULL && h->esq->esq != NULL && h->esq->esq->info > h->info)
        h = rotacionaDireita_B(h);

    return h;
}

int alturaArvore_B(ArvB h)
{
    if (h == NULL)
        return 0;
    int alturaEsq = alturaArvore_B(h->esq);
    int alturaDir = alturaArvore_B(h->dir);
    return (alturaEsq > alturaDir ? alturaEsq : alturaDir) + 1;
}

int main()
{
    ArvRN raiz_RN = NULL;
    ArvB raiz_B = NULL;
    srand(time(NULL));

    for (int i = 0; i < 10000; i++)
    {
        int num = rand() % 100000;
        raiz_RN = insere_RubroNegra(raiz_RN, num);
        raiz_B = insereNO_B(raiz_B, num);
    }

    int altura_RN = alturaArvore_RN(raiz_RN);
    int altura_B = alturaArvore_B(raiz_B);
    printf("Altura da arvore Rubro-Negra: %d\n", altura_RN);
    printf("Altura da arvore Preta: %d\n", altura_B);

    printf("Pressione Enter para sair..."); 
    getchar();
    return 0;
}
