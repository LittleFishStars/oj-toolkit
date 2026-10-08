#include <stdio.h>

int depth[20];

int main() {
    int N;
    scanf("%d", &N);
    depth[1] = 0;
    for (int i = 1; i < N; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        depth[v] = depth[u] + 1;
    }
    for (int i = 1; i <= N; i++)
        printf("%d\n", depth[i]);
    return 0;
}
