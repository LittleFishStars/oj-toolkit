C语言
```c
#include <stdio.h>

int mat[15][50];

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    for (int j = 0; j < M; j++) {
        int u, v;
        scanf("%d %d", &u, &v);
        mat[u - 1][j] = 1;
        mat[v - 1][j] = 1;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            printf("%d%c", mat[i][j], " \n"[j == M - 1]);
        }
    }
    return 0;
}
```

Python
```python
N, M = map(int, input().split())
mat = [[0] * M for _ in range(N)]
for j in range(M):
    u, v = map(int, input().split())
    mat[u - 1][j] = 1
    mat[v - 1][j] = 1
for row in mat:
    print(*row)
```
