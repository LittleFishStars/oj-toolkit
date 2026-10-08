C语言
```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    double s = 1.0 / (n * n);
    while (--n) s += 1.0 / (n * n);
    printf("%.6f\n", s);
    return 0;
}
```

Python
```python
print(f"{sum([1.0 / (i * i) for i in range(1, int(input()) + 1)]):.6f}")
```
