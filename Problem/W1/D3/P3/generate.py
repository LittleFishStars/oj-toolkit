from generator import Generator
import random

class ProblemW1D3P3(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["4 4 4", "9 1 1", "1 1 9", "1000000 1 500000"]
        if i < len(fixed):
            return fixed[i]
        a, b, c = random.randint(1, 1000000), random.randint(1, 1000000), random.randint(1, 1000000)
        return f"{a} {b} {c}"

    def generate_output(self, input_data: str) -> str:
        a, b, c = map(int, input_data.split())
        return str(max(a, b, c))

problem_generator = ProblemW1D3P3(test_num=10)
problem_generator.generate()
