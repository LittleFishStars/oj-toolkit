C语言
```c
#include <stdio.h>
#include <stdlib.h>

int cmp_asc(const void *a, const void *b) { return *(int *)a - *(int *)b; }
int cmp_desc(const void *a, const void *b) { return *(int *)b - *(int *)a; }

int main() {
    int n;
    scanf("%d", &n);
    int *odds = malloc(n * sizeof(int));
    int *evens = malloc(n * sizeof(int));
    int oc = 0, ec = 0;
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        if (x % 2) odds[oc++] = x;
        else evens[ec++] = x;
    }
    qsort(odds, oc, sizeof(int), cmp_asc);
    qsort(evens, ec, sizeof(int), cmp_desc);
    for (int i = 0; i < oc; i++)
        printf("%s%d", i ? " " : "", odds[i]);
    printf("\n");
    for (int i = 0; i < ec; i++)
        printf("%s%d", i ? " " : "", evens[i]);
    printf("\n");
    free(odds);
    free(evens);
    return 0;
}
```

Python
```python
n = int(input())
nums = list(map(int, input().split()))
odds = sorted(x for x in nums if x % 2 == 1)
evens = sorted((x for x in nums if x % 2 == 0), reverse=True)
print(" ".join(map(str, odds)))
print(" ".join(map(str, evens)))
```
