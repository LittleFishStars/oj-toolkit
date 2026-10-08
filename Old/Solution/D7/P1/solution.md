C语言
```c
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
```

Python
```python
L, M = map(int, input().split())
trees = [1] * (L + 1)
for _ in range(M):
    u, v = map(int, input().split())
    for j in range(u, v + 1):
        trees[j] = 0
print(sum(trees))
```
