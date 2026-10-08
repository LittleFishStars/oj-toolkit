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

    printf("2");

    if (n == 2) {
        printf("\n");
        return 0;
    }

    int k = (n - 1) / 2;
    char* marked = (char*)malloc(k + 1);
    memset(marked, 0, k + 1);

    for (int i = 1; i <= k; i++) {
        for (int j = i; i + j + 2 * i * j <= k; j++) {
            marked[i + j + 2 * i * j] = 1;
        }
    }

    for (int i = 1; i <= k; i++) {
        if (!marked[i]) {
            printf(" %d", 2 * i + 1);
        }
    }
    printf("\n");

    free(marked);
    return 0;
}
