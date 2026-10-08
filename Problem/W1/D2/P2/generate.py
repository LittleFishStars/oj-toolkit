from generator import Generator
import random

class ProblemW1D2P2(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["17 5", "10 2", "7 7", "1000000 3"]
        if i < len(fixed):
            return fixed[i]
        b = random.randint(1, 1000)
        a = random.randint(b, 1000000)
        return f"{a} {b}"

    def generate_output(self, input_data: str) -> str:
        a, b = map(int, input_data.split())
        return f"{a // b}\n{a % b}"

problem_generator = ProblemW1D2P2(test_num=10)
problem_generator.generate()
