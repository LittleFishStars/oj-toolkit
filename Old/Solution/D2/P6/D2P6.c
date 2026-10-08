#include <stdio.h>

int main() {
    int k, n = 0;
    double s = 0.0;
    scanf("%d", &k);
    while (s <= k) {
        n++;
        s += 1.0 / n;
    }
    printf("%d\n", n);
    return 0;
}
