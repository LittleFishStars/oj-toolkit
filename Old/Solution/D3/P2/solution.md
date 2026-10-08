C语言
```c
#include <stdio.h>

int main() {
    int n, x, mx;
    scanf("%d", &n);
    scanf("%d", &mx);
    for (int i = 1; i < n; i++) {
        scanf("%d", &x);
        if (x > mx) mx = x;
    }
    printf("%d\n", mx);
    return 0;
}
```

Python
```python
input()
print(max(map(int, input().split())))
```
