C语言
```c
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
```

Python
```python
N = int(input())
parent = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    parent[v] = u
for i in range(1, N + 1):
    print(parent[i])
```
