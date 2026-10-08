from generator import Generator
import random
import string

class D1P5(Generator):
    def generate_input(self) -> str:
        return random.choice(string.printable.strip())

    def generate_output(self, input_data: str) -> str:
        return str(ord(input_data))

problem_generator = D1P5(test_num=10)
problem_generator.generate()
