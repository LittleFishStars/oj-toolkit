#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    double s = 1.0 / n;
    while (--n) s += 1.0 / n;
    printf("%.6f\n", s);
    return 0;
}
