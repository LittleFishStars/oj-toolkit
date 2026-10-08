#include <stdio.h>

int children[20][20], sz[20];
int size[20], order[20], o_n;

void dfs(int u) {
    order[o_n++] = u;
    for (int i = 0; i < sz[u]; i++)
        dfs(children[u][i]);
}

int main() {
    int N;
    scanf("%d", &N);
    for (int i = 1; i < N; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        children[u][sz[u]++] = v;
    }
    o_n = 0;
    dfs(1);
    for (int i = 1; i <= N; i++) size[i] = 1;
    for (int i = o_n - 1; i >= 0; i--) {
        int u = order[i];
        for (int j = 0; j < sz[u]; j++)
            size[u] += size[children[u][j]];
    }
    for (int i = 1; i <= N; i++)
        printf("%d\n", size[i]);
    return 0;
}
