#include <stdio.h>

int main() {
    int balance = 0, savings = 0;
    for (int i = 1; i <= 12; i++) {
        int budget;
        scanf("%d", &budget);
        balance += 300;
        if (balance < budget) {
            printf("-%d\n", i);
            return 0;
        }
        balance -= budget;
        int deposit = balance / 100 * 100;
        savings += deposit;
        balance -= deposit;
    }
    printf("%d\n", savings + savings / 5 + balance);
    return 0;
}
