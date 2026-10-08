C语言
```c
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
```

Python
```python
N, M = map(int, input().split())
deg = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    deg[u - 1] += 1
    deg[v - 1] += 1
for d in deg:
    print(d)
```
