from generator import Generator
import random

class ProblemW1D6P3(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["2024 2 29", "2023 2 29", "2023 13 1", "2023 4 31", "2000 2 29", "1900 2 29", "2023 12 31"]
        if i < len(fixed):
            return fixed[i]
        y = random.randint(1, 3000)
        m = random.randint(1, 14)
        d = random.randint(1, 32)
        return f"{y} {m} {d}"

    def generate_output(self, input_data: str) -> str:
        y, m, d = map(int, input_data.split())
        if m < 1 or m > 12 or d < 1:
            return "No"
        leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
        days = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return "Yes" if d <= days[m - 1] else "No"

problem_generator = ProblemW1D6P3(test_num=10)
problem_generator.generate()
