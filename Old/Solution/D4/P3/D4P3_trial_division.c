#include <stdio.h>

int is_prime(int n) {
    if (n < 2) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int d = 3; d * d <= n; d += 2) {
        if (n % d == 0) return 0;
    }
    return 1;
}

int main() {
    int p;
    scanf("%d", &p);

    int idx = 0;
    for (int i = 2; i <= p; i++) {
        if (is_prime(i)) {
            idx++;
            if (i == p) {
                printf("%d\n", idx);
                return 0;
            }
        }
    }
}
