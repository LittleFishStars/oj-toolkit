#include <stdio.h>

int trees[10005];

int main() {
    int L, M;
    scanf("%d %d", &L, &M);
    for (int i = 0; i <= L; i++)
        trees[i] = 1;
    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        for (int j = u; j <= v; j++)
            trees[j] = 0;
    }
    int ans = 0;
    for (int i = 0; i <= L; i++)
        ans += trees[i];
    printf("%d\n", ans);
    return 0;
}
