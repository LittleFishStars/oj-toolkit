#include <stdio.h>

int main() {
    int apples[10];
    for (int i = 0; i < 10; i++)
        scanf("%d", &apples[i]);
    int hand;
    scanf("%d", &hand);
    int reach = hand + 30;
    int ans = 0;
    for (int i = 0; i < 10; i++)
        if (apples[i] <= reach)
            ans++;
    printf("%d\n", ans);
    return 0;
}
