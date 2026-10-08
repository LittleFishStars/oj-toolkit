C语言
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int p;
    scanf("%d", &p);

    char* is_prime = (char*)malloc(p + 1);
    memset(is_prime, 1, p + 1);
    is_prime[0] = is_prime[1] = 0;

    for (int i = 2; i * i <= p; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= p; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    int idx = 0;
    for (int i = 2; i <= p; i++) {
        if (is_prime[i]) {
            idx++;
            if (i == p) {
                printf("%d\n", idx);
                break;
            }
        }
    }

    free(is_prime);
    return 0;
}
```

Python
```python
p = int(input())
is_prime = [True] * (p + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(p ** 0.5) + 1):
    if is_prime[i]:
        is_prime[i * i:p + 1:i] = [False] * ((p - i * i) // i + 1)
idx = 0
for i in range(2, p + 1):
    if is_prime[i]:
        idx += 1
        if i == p:
            print(idx)
            break
```
