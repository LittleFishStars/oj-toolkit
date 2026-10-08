C语言
```c
#include <stdio.h>
#include <string.h>

int adj[15][15];
int sz[15];

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--;
        adj[u][sz[u]++] = v;
        adj[v][sz[v]++] = u;
    }
    for (int i = 0; i < N; i++) {
        printf("%d:", i + 1);
        if (sz[i] > 0) {
            // bubble sort for small N
            for (int a = 0; a < sz[i] - 1; a++)
                for (int b = 0; b < sz[i] - 1 - a; b++)
                    if (adj[i][b] > adj[i][b + 1]) {
                        int t = adj[i][b];
                        adj[i][b] = adj[i][b + 1];
                        adj[i][b + 1] = t;
                    }
            for (int j = 0; j < sz[i]; j++)
                printf(" %d", adj[i][j] + 1);
        }
        printf("\n");
    }
    return 0;
}
```

Python
```python
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u - 1].append(v)
    adj[v - 1].append(u)
for i in range(N):
    adj[i].sort()
    if adj[i]:
        print(f"{i + 1}:", *adj[i])
    else:
        print(f"{i + 1}:")
```
