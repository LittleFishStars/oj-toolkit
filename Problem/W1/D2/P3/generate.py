from generator import Generator
import random

class ProblemW1D2P3(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["2", "1.5", "1", "100", "0.5"]
        if i < len(fixed):
            return fixed[i]
        r = random.randint(1, 1000) / 10
        return str(r)

    def generate_output(self, input_data: str) -> str:
        r = float(input_data)
        pi = 3.14159
        return f"{pi * r * r:.2f}\n{2 * pi * r:.2f}"

problem_generator = ProblemW1D2P3(test_num=10)
problem_generator.generate()
