from generator import Generator
import random

class D2P4(Generator):
    def generate_input(self) -> str:
        return str(random.randint(1, 1000))

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        return str(n * n)

problem_generator = D2P4(test_num=10)
problem_generator.generate()
