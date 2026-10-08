#include <stdio.h>

int deg[15];

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        deg[u - 1]++;
        deg[v - 1]++;
    }
    for (int i = 0; i < N; i++)
        printf("%d\n", deg[i]);
    return 0;
}
