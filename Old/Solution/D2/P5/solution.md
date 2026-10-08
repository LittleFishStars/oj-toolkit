C语言
```c
#include <stdio.h>

int main() {
    int n, x, sum = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        sum += x;
    }
    printf("%d\n", sum);
    printf("%.2f\n", (float)sum / n);
    return 0;
}
```

Python
```python
n = int(input())
total = sum(map(int, input().split()))
print(total)
print(f"{total / n:.2f}")
```
