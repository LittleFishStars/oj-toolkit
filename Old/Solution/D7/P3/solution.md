C语言
```c
#include <stdio.h>

int main() {
    int max_hours = 0, max_day = 0;
    for (int i = 1; i <= 7; i++) {
        int school, extra;
        scanf("%d %d", &school, &extra);
        int total = school + extra;
        if (total > max_hours) {
            max_hours = total;
            max_day = i;
        }
    }
    if (max_hours <= 8)
        printf("0\n");
    else
        printf("%d\n", max_day);
    return 0;
}
```

Python
```python
max_hours = 0
max_day = 0
for i in range(1, 8):
    school, extra = map(int, input().split())
    total = school + extra
    if total > max_hours:
        max_hours = total
        max_day = i
print(0 if max_hours <= 8 else max_day)
```
