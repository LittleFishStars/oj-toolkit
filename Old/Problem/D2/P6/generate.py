from generator import Generator
import random

class D2P6(Generator):
    def generate_input(self) -> str:
        return str(random.randint(1, 5))

    def generate_output(self, input_data: str) -> str:
        k = int(input_data)
        s = 0.0
        n = 0
        while s <= k:
            n += 1
            s += 1 / n
        return str(n)

problem_generator = D2P6(test_num=10)
problem_generator.generate()
