from generator import Generator
import random


class ProblemW3D5P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["12 25 10", "1 1 0", "1 1 30", "6 30 1", "12 30 10000"]
        if i < len(fixed):
            return fixed[i]
        m = random.randint(1, 12)
        d = random.randint(1, 30)
        k = random.randint(0, 10000)
        return f"{m} {d} {k}"

    def generate_output(self, input_data: str) -> str:
        m, d, k = map(int, input_data.split())
        total = (m - 1) * 30 + (d - 1) + k
        total %= 360
        return f"{total // 30 + 1}/{total % 30 + 1}"


problem_generator = ProblemW3D5P3(test_num=10)
problem_generator.generate()
