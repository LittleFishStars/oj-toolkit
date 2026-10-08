C语言
```c
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
```

Python
```python
N = int(input())
has_child = [False] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    has_child[u] = True
print(sum(1 for i in range(1, N + 1) if not has_child[i]))
```
