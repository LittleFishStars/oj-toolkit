from generator import Generator
import random


class ProblemW3D2P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["3 4 5", "2 2 2", "6 8 10", "1 1 1", "1000 1000 1"]
        if i < len(fixed):
            return fixed[i]
        a = random.randint(1, 1000)
        b = random.randint(max(1, a - 400), min(1000, a + 400))
        c = random.randint(abs(a - b) + 1, a + b - 1)
        c = min(c, 1000)
        if c <= abs(a - b):
            c = abs(a - b) + 1
        return f"{a} {b} {c}"

    def generate_output(self, input_data: str) -> str:
        a, b, c = map(int, input_data.split())
        perimeter = a + b + c
        p = perimeter / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return f"{perimeter}\n{area:.2f}"


problem_generator = ProblemW3D2P3(test_num=10)
problem_generator.generate()
