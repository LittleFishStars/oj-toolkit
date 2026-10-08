balance = 0
savings = 0
for i in range(1, 13):
    budget = int(input())
    balance += 300
    if balance < budget:
        print(f"-{i}")
        exit()
    balance -= budget
    deposit = balance // 100 * 100
    savings += deposit
    balance -= deposit
print(savings + savings // 5 + balance)
