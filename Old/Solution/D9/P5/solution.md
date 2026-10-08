C语言
```c
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
```

Python
```python
N = int(input())
children = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    children[u].append(v)

size = [1] * (N + 1)
order = []

def dfs(u):
    order.append(u)
    for v in children[u]:
        dfs(v)

dfs(1)
for u in reversed(order):
    for v in children[u]:
        size[u] += size[v]

for i in range(1, N + 1):
    print(size[i])
```
