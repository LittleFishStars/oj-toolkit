C语言
```c
#include <stdio.h>

int adj[15][15];

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--;
        adj[u][v] = 1;
        adj[v][u] = 1;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d%c", adj[i][j], " \n"[j == N - 1]);
        }
    }
    return 0;
}
```

Python
```python
N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u - 1][v - 1] = 1
    adj[v - 1][u - 1] = 1
for row in adj:
    print(*row)
```
