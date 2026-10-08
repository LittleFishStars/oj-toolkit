C语言
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[64];
    int age;
    int idx;
} Entry;

int cmp(const void *a, const void *b) {
    Entry *ea = (Entry *)a, *eb = (Entry *)b;
    int nc = strcmp(ea->name, eb->name);
    if (nc != 0) return nc;
    if (ea->age != eb->age) return ea->age - eb->age;
    return ea->idx - eb->idx;
}

int main() {
    int n;
    scanf("%d", &n);
    Entry *e = malloc(n * sizeof(Entry));
    for (int i = 0; i < n; i++) {
        scanf("%s %d", e[i].name, &e[i].age);
        e[i].idx = i;
    }
    qsort(e, n, sizeof(Entry), cmp);
    for (int i = 0; i < n; i++)
        printf("%s %d\n", e[i].name, e[i].age);
    free(e);
    return 0;
}
```

Python
```python
n = int(input())
entries = []
for i in range(n):
    name, age = input().split()
    entries.append((name, int(age), i))
entries.sort(key=lambda x: (x[0], x[1], x[2]))
for name, age, _ in entries:
    print(name, age)
```
