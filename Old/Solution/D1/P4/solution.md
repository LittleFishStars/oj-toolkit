C语言
```c
#include <stdio.h>

int main() {
    double a, b;
    scanf("%lf %lf", &a, &b);
    printf("%.2f\n", a + b);
    return 0;
}
```

Python
```python
print(f"{sum(map(float, input().split(','))):.2f}")
```
