#include <stdio.h>

int main() {
    int n, x, cnt = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x % 2 == 0) cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}
