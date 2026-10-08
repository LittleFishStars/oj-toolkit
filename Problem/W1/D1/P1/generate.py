from generator import Generator
import random

class ProblemW1D1P1(Generator):
    def generate_input(self) -> str:
        return ""

    def generate_output(self, input_data: str) -> str:
        return "Hello, World!"

problem_generator = ProblemW1D1P1(test_num=3)
problem_generator.generate()
