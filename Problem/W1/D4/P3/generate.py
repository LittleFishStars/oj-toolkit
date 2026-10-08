from generator import Generator
import random

class ProblemW1D4P3(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["3 4 5", "1 2 3", "6 6 6", "5 5 8", "10 1 1", "2 2 5"]
        if i < len(fixed):
            return fixed[i]
        a, b, c = random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)
        return f"{a} {b} {c}"

    def generate_output(self, input_data: str) -> str:
        a, b, c = sorted(map(int, input_data.split()))
        if a + b <= c:
            return "不能构成三角形"
        if a == b == c:
            return "等边三角形"
        if a == b or b == c:
            return "等腰三角形"
        return "普通三角形"

problem_generator = ProblemW1D4P3(test_num=10)
problem_generator.generate()
