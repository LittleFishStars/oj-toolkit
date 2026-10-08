from generator import Generator
import random

class ProblemW1D2P1(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["5\n3", "0\n0", "10\n10", "0\n999"]
        if i < len(fixed):
            return fixed[i]
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        return f"{a}\n{b}"

    def generate_output(self, input_data: str) -> str:
        a, b = map(int, input_data.split())
        return f"Add {a + b}\nSub {a - b}\nMul {a * b}"

problem_generator = ProblemW1D2P1(test_num=10)
problem_generator.generate()
