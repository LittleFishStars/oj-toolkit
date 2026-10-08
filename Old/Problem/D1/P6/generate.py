from generator import Generator
import random

class D1P6(Generator):
    def generate_input(self) -> str:
        return str(random.randint(32, 126))

    def generate_output(self, input_data: str) -> str:
        return chr(int(input_data))

problem_generator = D1P6(test_num=10)
problem_generator.generate()
