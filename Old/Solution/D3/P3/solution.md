C语言
```c
#include <stdio.h>

int main() {
    int n, k, x, cnt = 0;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x == k) cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}
```

Python
```python
_, k = map(int, input().split())
print(sum(1 for x in map(int, input().split()) if x == k))
```
