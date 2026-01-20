#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_VERTICES 100

typedef struct
{
    int vertice;
    int peso;
} Aresta;

typedef struct
{
    int numVertices;
    int grau[MAX_VERTICES];
    Aresta *arestas[MAX_VERTICES];
} Grafo;

int procuraMenorDistancia(float *dist, int *visitado, int NV)
{
    int i, menor = -1, primeiro = 1;
    for (i = 0; i < NV; i++)
    {
        if (dist[i] >= 0 && visitado[i] == 0)
        {
            if (primeiro)
            {
                menor = i;
                primeiro = 0;
            }
            else
            {
                if (dist[menor] > dist[i])
                    menor = i;
            }
        }
    }
    return menor;
}

void menorCaminho_Grafo(Grafo *gr, int ini, int *ant, float *dist)
{
    int i, cont, NV, ind, *visitado, vert;
    cont = NV = gr->numVertices;
    visitado = (int *)malloc(NV * sizeof(int));
    for (i = 0; i < NV; i++)
    {
        ant[i] = -1;
        dist[i] = -1;
        visitado[i] = 0;
    }
    dist[ini] = 0;
    while (cont > 0)
    {
        vert = procuraMenorDistancia(dist, visitado, NV);
        if (vert == -1)
            break;
        visitado[vert] = 1;
        cont--;
        for (i = 0; i < gr->grau[vert]; i++)
        {
            ind = gr->arestas[vert][i].vertice;
            float peso = gr->arestas[vert][i].peso;
            if (dist[ind] < 0)
            {
                dist[ind] = dist[vert] + peso;
                ant[ind] = vert;
            }
            else
            {
                if (dist[ind] > dist[vert] + peso)
                {
                    dist[ind] = dist[vert] + peso;
                    ant[ind] = vert;
                }
            }
        }
    }
    free(visitado);
}

void adicionarAresta(Grafo *gr, int origem, int destino, int peso)
{
    gr->arestas[origem] = (Aresta*) realloc(gr->arestas[origem], (gr->grau[origem] + 1) * sizeof(Aresta)); // Cast para Aresta*
    gr->arestas[origem][gr->grau[origem]].vertice = destino;
    gr->arestas[origem][gr->grau[origem]].peso = peso;
    gr->grau[origem]++;
}

int main()
{
    Grafo grafo;
    grafo.numVertices = 6; // Exemplo com 6 vértices (A, B, C, D, E, F)
    for (int i = 0; i < grafo.numVertices; i++)
    {
        grafo.grau[i] = 0;
        grafo.arestas[i] = NULL;
    }

    adicionarAresta(&grafo, 0, 1, 6); // A -> B
    adicionarAresta(&grafo, 0, 2, 3); // A -> C
    adicionarAresta(&grafo, 1, 2, 2); // B -> C
    adicionarAresta(&grafo, 1, 3, 5); // B -> D
    adicionarAresta(&grafo, 2, 3, 3); // C -> D
    adicionarAresta(&grafo, 2, 4, 4); // C -> E
    adicionarAresta(&grafo, 3, 4, 2); // D -> E
    adicionarAresta(&grafo, 3, 5, 3); // D -> F
    adicionarAresta(&grafo, 4, 5, 5); // E -> F

    int ant[MAX_VERTICES];
    float dist[MAX_VERTICES];
    menorCaminho_Grafo(&grafo, 0, ant, dist); // Menor caminho a partir do vértice A (índice 0)

    printf("Menores distancias a partir do vertice A:\n");
    for (int i = 0; i < grafo.numVertices; i++)
    {
        printf("Para %c: %.1f\n", 'A' + i, dist[i]);
    }

    for (int i = 0; i < grafo.numVertices; i++)
    {
        free(grafo.arestas[i]);
    }

    printf("Pressione Enter para sair..."); 
    getchar();
    return 0;
}
