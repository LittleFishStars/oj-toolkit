from generator import Generator
import random


class ProblemW3D2P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["3 4", "1 1", "1000 1000", "1 1000", "7 2"]
        if i < len(fixed):
            return fixed[i]
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        return f"{a} {b}"

    def generate_output(self, input_data: str) -> str:
        a, b = map(int, input_data.split())
        return f"{a * b}\n{2 * (a + b)}"


problem_generator = ProblemW3D2P1(test_num=10)
problem_generator.generate()
