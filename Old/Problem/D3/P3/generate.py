from generator import Generator
import random

class D3P3(Generator):
    def generate_input(self) -> str:
        n = random.randint(3, 20)
        c = random.randint(0, n)
        k = random.randint(1, 100)
        numbers = [k] * c
        for _ in range(n - c):
            x = random.randint(1, 100)
            while x == k:
                x = random.randint(1, 100)
            numbers.append(x)
        random.shuffle(numbers)
        return f"{n} {k}\n{' '.join(map(str, numbers))}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        n, k = map(int, lines[0].split())
        numbers = list(map(int, lines[1].split()))
        return str(numbers.count(k))

problem_generator = D3P3(test_num=10)
problem_generator.generate()
