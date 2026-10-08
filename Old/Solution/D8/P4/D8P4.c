#include <stdio.h>

struct Edge {
    int u, v;
} edges[100];

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        if (u > v) { int t = u; u = v; v = t; }
        edges[i].u = u;
        edges[i].v = v;
    }
    // bubble sort
    for (int i = 0; i < M - 1; i++)
        for (int j = 0; j < M - 1 - i; j++)
            if (edges[j].u > edges[j + 1].u ||
               (edges[j].u == edges[j + 1].u && edges[j].v > edges[j + 1].v)) {
                struct Edge t = edges[j];
                edges[j] = edges[j + 1];
                edges[j + 1] = t;
            }
    for (int i = 0; i < M; i++)
        printf("%d %d\n", edges[i].u, edges[i].v);
    return 0;
}
