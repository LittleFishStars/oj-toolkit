C语言
```c
#include <stdio.h>

int main() {
    int n, x, cnt = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x % 2 == 0) cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}
```

Python
```python
input()
print(sum(1 for x in map(int, input().split()) if x % 2 == 0))
```
