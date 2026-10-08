#include <stdio.h>

int has_child[20];

int main() {
    int N;
    scanf("%d", &N);
    for (int i = 1; i < N; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        has_child[u] = 1;
    }
    int leaf = 0;
    for (int i = 1; i <= N; i++)
        if (!has_child[i]) leaf++;
    printf("%d\n", leaf);
    return 0;
}
