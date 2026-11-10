Python
```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, x):
        self.balance += x
        return self.balance

    def withdraw(self, x):
        if x > self.balance:
            return "no"
        self.balance -= x
        return self.balance


balance = int(input())
m = int(input())
acc = Account(balance)
for _ in range(m):
    kind, x = input().split()
    if kind == "deposit":
        print(acc.deposit(int(x)))
    else:
        print(acc.withdraw(int(x)))
```
