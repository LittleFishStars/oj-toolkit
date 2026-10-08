#include <stdio.h>

#define MAXN 55

int stack[MAXN];
int top;

int main() {
    int n;
    scanf("%d", &n);
    top = 0;
    for (int i = 0; i < n; i++) {
        int op, x;
        scanf("%d", &op);
        if (op == 1) {
            scanf("%d", &x);
            stack[top++] = x;
        } else if (op == 2) {
            if (top > 0) {
                printf("%d\n", stack[--top]);
            } else {
                printf("Empty\n");
            }
        } else if (op == 3) {
            if (top > 0) {
                printf("%d\n", stack[top - 1]);
            } else {
                printf("Empty\n");
            }
        } else if (op == 4) {
            printf("%d\n", top);
        }
    }
    return 0;
}
