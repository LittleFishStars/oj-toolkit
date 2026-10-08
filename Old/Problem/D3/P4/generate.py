from generator import Generator
import random

class D3P4(Generator):
    def generate_input(self) -> str:
        n = random.randint(3, 20)
        numbers = [random.randint(1, 100) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, numbers))}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        n = int(lines[0])
        numbers = list(map(int, lines[1].split()))
        count = 0
        for i in range(1, n - 1):
            if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
                count += 1
        return str(count)

problem_generator = D3P4(test_num=10)
problem_generator.generate()
