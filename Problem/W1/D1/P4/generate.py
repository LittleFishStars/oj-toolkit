from generator import Generator
import random

class ProblemW1D1P4(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        if i == 0:
            return "1 2"
        if i == 1:
            return "0 0"
        if i == 2:
            return "1000000 1000000"
        a = random.randint(0, 1000000)
        b = random.randint(0, 1000000)
        return f"{a} {b}"

    def generate_output(self, input_data: str) -> str:
        a, b = map(int, input_data.split())
        return str(a + b)

problem_generator = ProblemW1D1P4(test_num=10)
problem_generator.generate()
