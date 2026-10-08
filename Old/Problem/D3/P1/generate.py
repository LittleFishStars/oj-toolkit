from generator import Generator
import random

class D3P1(Generator):
    def generate_input(self) -> str:
        n = random.randint(1, 20)
        numbers = [random.randint(1, 100) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, numbers))}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        numbers = list(map(int, lines[1].split()))
        return str(sum(1 for x in numbers if x % 2 == 0))

problem_generator = D3P1(test_num=10)
problem_generator.generate()
