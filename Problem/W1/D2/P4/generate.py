from generator import Generator
import random

class ProblemW1D2P4(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["80 90 85", "77.5 88 92.5", "0 0 0", "100 100 100"]
        if i < len(fixed):
            return fixed[i]
        s = [str(random.randint(0, 1000) / 10) for _ in range(3)]
        return " ".join(s)

    def generate_output(self, input_data: str) -> str:
        a, b, c = map(float, input_data.split())
        return f"{(a + b + c) / 3:.2f}"

problem_generator = ProblemW1D2P4(test_num=10)
problem_generator.generate()
