from generator import Generator
import random


class ProblemW3D4P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["1 6\n1 3", "2 4\n2 4", "1 2\n1 3", "1 1000\n1000 1000", "3 9\n2 9"]
        if i < len(fixed):
            return fixed[i]
        a = [random.randint(1, 1000) for _ in range(4)]
        return f"{a[0]} {a[1]}\n{a[2]} {a[3]}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        p1, q1 = map(int, lines[0].split())
        p2, q2 = map(int, lines[1].split())
        p = p1 * q2 + p2 * q1
        q = q1 * q2
        a, b = p, q
        while b:
            a, b = b, a % b
        return f"{p // a}/{q // a}"


problem_generator = ProblemW3D4P2(test_num=10)
problem_generator.generate()
