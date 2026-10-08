C语言
```c
#include <stdio.h>

int children[20][20];
int sz[20];

int main() {
    int N;
    scanf("%d", &N);
    for (int i = 1; i < N; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        children[u][sz[u]++] = v;
    }
    for (int i = 1; i <= N; i++) {
        printf("%d:", i);
        if (sz[i] > 0) {
            for (int a = 0; a < sz[i] - 1; a++)
                for (int b = 0; b < sz[i] - 1 - a; b++)
                    if (children[i][b] > children[i][b + 1]) {
                        int t = children[i][b];
                        children[i][b] = children[i][b + 1];
                        children[i][b + 1] = t;
                    }
            for (int j = 0; j < sz[i]; j++)
                printf(" %d", children[i][j]);
        }
        printf("\n");
    }
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
for i in range(1, N + 1):
    children[i].sort()
    if children[i]:
        print(f"{i}:", *children[i])
    else:
        print(f"{i}:")
```
