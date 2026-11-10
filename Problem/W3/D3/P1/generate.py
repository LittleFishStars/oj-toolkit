from generator import Generator
import random


class ProblemW3D3P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["dog", "cat", "dog", "cat", "cat"]
        if i < len(fixed):
            return fixed[i]
        return random.choice(["dog", "cat"])

    def generate_output(self, input_data: str) -> str:
        word = input_data.strip()
        return "wang" if word == "dog" else "miao"


problem_generator = ProblemW3D3P1(test_num=10)
problem_generator.generate()
