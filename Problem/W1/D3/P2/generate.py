from generator import Generator
import random

class ProblemW1D3P2(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = [7, 0, 1, 2, 999999]
        n = fixed[i] if i < len(fixed) else random.randint(0, 1000000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        return "偶数" if n % 2 == 0 else "奇数"

problem_generator = ProblemW1D3P2(test_num=10)
problem_generator.generate()
