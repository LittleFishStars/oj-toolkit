from generator import Generator
import random

class D2P1(Generator):
    def generate_input(self) -> str:
        n = random.randint(1, 1000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        return str(n * (n + 1) // 2)

problem_generator = D2P1(test_num=10)
problem_generator.generate()
