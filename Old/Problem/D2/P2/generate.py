from generator import Generator
import random

class D2P2(Generator):
    def generate_input(self) -> str:
        return str(random.randint(1, 15))

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        s = sum(1 / i for i in range(1, n + 1))
        return f"{s:.6f}"

problem_generator = D2P2(test_num=10)
problem_generator.generate()
