C语言
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);

    if (n < 2) {
        printf("\n");
        return 0;
    }

    char* is_prime = (char*)malloc(n + 1);
    memset(is_prime, 1, n + 1);
    is_prime[0] = is_prime[1] = 0;

    for (int i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    int first = 1;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) {
            if (!first) printf(" ");
            printf("%d", i);
            first = 0;
        }
    }
    printf("\n");

    free(is_prime);
    return 0;
}
```

Python
```python
n = int(input())
if n < 2:
    print()
    exit()
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        is_prime[i * i:n + 1:i] = [False] * ((n - i * i) // i + 1)
print(' '.join(str(i) for i in range(2, n + 1) if is_prime[i]))
```
