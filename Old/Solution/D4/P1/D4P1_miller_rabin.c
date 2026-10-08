#include <stdio.h>

int pow_mod(int a, int e, int m) {
    int result = 1;
    a %= m;
    while (e) {
        if (e & 1) result = (long long)result * a % m;
        a = (long long)a * a % m;
        e >>= 1;
    }
    return result;
}

int is_prime(int n) {
    if (n < 2) return 0;
    if (n == 2 || n == 3) return 1;
    if (n % 2 == 0) return 0;

    int d = n - 1;
    int s = 0;
    while (d % 2 == 0) {
        d /= 2;
        s++;
    }

    int bases[] = {2, 7, 61};
    for (int i = 0; i < 3; i++) {
        int a = bases[i];
        if (a >= n) continue;
        int x = pow_mod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        int composite = 1;
        for (int r = 0; r < s - 1; r++) {
            x = (long long)x * x % n;
            if (x == n - 1) {
                composite = 0;
                break;
            }
        }
        if (composite) return 0;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);

    int count = 0;
    for (int i = 2; ; i++) {
        if (is_prime(i)) {
            count++;
            if (count == n) {
                printf("%d\n", i);
                return 0;
            }
        }
    }
}
