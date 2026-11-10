from generator import Generator
import random


class ProblemW3D4P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["1 2\n3 4", "-1 1\n1 -1", "0 0\n0 0", "1000 1000\n-1000 -1000"]
        if i < len(fixed):
            return fixed[i]
        a = [random.randint(-1000, 1000) for _ in range(4)]
        return f"{a[0]} {a[1]}\n{a[2]} {a[3]}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        x1, y1 = map(int, lines[0].split())
        x2, y2 = map(int, lines[1].split())
        return f"({x1 + x2},{y1 + y2})"


problem_generator = ProblemW3D4P1(test_num=10)
problem_generator.generate()
