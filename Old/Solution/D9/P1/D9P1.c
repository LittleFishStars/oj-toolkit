#include <stdio.h>

int parent[20];

int main() {
    int N;
    scanf("%d", &N);
    for (int i = 1; i < N; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        parent[v] = u;
    }
    for (int i = 1; i <= N; i++)
        printf("%d\n", parent[i]);
    return 0;
}
