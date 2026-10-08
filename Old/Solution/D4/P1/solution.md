C语言
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);

    int limit = 10000000;
    if (n > 600000) limit = (int)((long long)n * 14);

    char* is_prime = (char*)malloc(limit + 1);
    memset(is_prime, 1, limit + 1);
    is_prime[0] = is_prime[1] = 0;

    for (int i = 2; i * i <= limit; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= limit; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    int count = 0;
    for (int i = 2; i <= limit; i++) {
        if (is_prime[i]) {
            count++;
            if (count == n) {
                printf("%d\n", i);
                free(is_prime);
                return 0;
            }
        }
    }

    free(is_prime);
    return 0;
}
```

Python
```python
n = int(input())
limit = max(1000000, n * 13)
is_prime = bytearray(b'\x01') * (limit + 1)
is_prime[0] = is_prime[1] = 0
for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        is_prime[i * i:limit + 1:i] = b'\x00' * ((limit - i * i) // i + 1)
cnt = 0
for i in range(2, limit + 1):
    if is_prime[i]:
        cnt += 1
        if cnt == n:
            print(i)
            break
```
