from generator import Generator
import random


class D7P4(Generator):
    def generate_input(self) -> str:
        budgets = []
        for _ in range(12):
            b = random.randint(0, 400)
            budgets.append(b)
        return "\n".join(map(str, budgets))

    def generate_output(self, input_data: str) -> str:
        budgets = list(map(int, input_data.strip().split("\n")))
        assert len(budgets) == 12

        balance = 0
        savings = 0

        for month in range(12):
            balance += 300
            if balance < budgets[month]:
                return f"-{month + 1}"
            balance -= budgets[month]
            deposit = (balance // 100) * 100
            savings += deposit
            balance -= deposit

        total = savings + savings // 5 + balance
        return str(total)


problem_generator = D7P4(test_num=10)
problem_generator.generate()
