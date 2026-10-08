C语言
```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) { return *(int *)a - *(int *)b; }

int main() {
    int n;
    scanf("%d", &n);
    int *a = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    qsort(a, n, sizeof(int), cmp);
    int prev = -1;
    int first = 1;
    for (int i = 0; i < n; i++) {
        if (a[i] != prev) {
            printf("%s%d", first ? "" : " ", a[i]);
            first = 0;
            prev = a[i];
        }
    }
    printf("\n");
    free(a);
    return 0;
}
```

Python
```python
input()
print(" ".join(map(str, sorted(set(map(int, input().split()))))))
```
