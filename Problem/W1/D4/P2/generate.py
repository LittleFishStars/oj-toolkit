from generator import Generator
import random

class ProblemW1D4P2(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = [2024, 1900, 2000, 2023, 2100, 4]
        y = fixed[i] if i < len(fixed) else random.randint(1, 3000)
        return str(y)

    def generate_output(self, input_data: str) -> str:
        y = int(input_data)
        ok = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
        return "闰年" if ok else "平年"

problem_generator = ProblemW1D4P2(test_num=10)
problem_generator.generate()
