from generator import Generator
import random

class ProblemW1D7P1(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["3 7", "5 5", "-1 1", "1000 -1000"]
        if i < len(fixed):
            return fixed[i]
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        return f"{a} {b}"

    def generate_output(self, input_data: str) -> str:
        a, b = map(int, input_data.split())
        return f"{b} {a}"

problem_generator = ProblemW1D7P1(test_num=10)
problem_generator.generate()
