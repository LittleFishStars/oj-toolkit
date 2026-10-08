from generator import Generator
import random

class D1P4(Generator):
    def generate_input(self) -> str:
        a = random.uniform(1, 1000)
        b = random.uniform(1, 1000)
        return f"{a} {b}"

    def generate_output(self, input_data: str) -> str:
        a, b = map(float, input_data.split())
        return f"{a + b:.2f}"

problem_generator = D1P4(test_num=10)
problem_generator.generate()
