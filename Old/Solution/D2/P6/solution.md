C语言
```c
#include <stdio.h>

int main() {
    int k, n = 0;
    double s = 0.0;
    scanf("%d", &k);
    while (s <= k) {
        n++;
        s += 1.0 / n;
    }
    printf("%d\n", n);
    return 0;
}
```

Python
```python
k = int(input())
s = 0.0
n = 0
while s <= k:
    n += 1
    s += 1.0 / n
print(n)
```
