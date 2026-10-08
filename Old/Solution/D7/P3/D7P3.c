#include <stdio.h>

int main() {
    int max_hours = 0, max_day = 0;
    for (int i = 1; i <= 7; i++) {
        int school, extra;
        scanf("%d %d", &school, &extra);
        int total = school + extra;
        if (total > max_hours) {
            max_hours = total;
            max_day = i;
        }
    }
    if (max_hours <= 8)
        printf("0\n");
    else
        printf("%d\n", max_day);
    return 0;
}
