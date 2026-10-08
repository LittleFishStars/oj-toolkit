from generator import Generator
import random

class D2P5(Generator):
    def generate_input(self) -> str:
        n = random.randint(1, 15)
        numbers = [random.randint(1, 100) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, numbers))}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        n = int(lines[0])
        numbers = list(map(int, lines[1].split()))
        total = sum(numbers)
        avg = total / n
        return f"{total}\n{avg:.2f}"

problem_generator = D2P5(test_num=10)
problem_generator.generate()
