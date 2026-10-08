from generator import Generator
import random

class ProblemW1D1P2(Generator):
    def generate_input(self) -> str:
        return ""

    def generate_output(self, input_data: str) -> str:
        return "我叫Python\n我今年1岁\n我最喜欢编程"

problem_generator = ProblemW1D1P2(test_num=3)
problem_generator.generate()
