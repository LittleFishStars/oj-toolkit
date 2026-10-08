from generator import Generator
import random

class D1P3(Generator):
    def generate_input(self) -> str:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        return f"{a},{b}"

    def generate_output(self, input_data: str) -> str:
        a, b = map(int, input_data.split(","))
        return f"{a + b}"

problem_generator = D1P3(test_num=10)
problem_generator.generate()
