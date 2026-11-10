from generator import Generator
import random


class ProblemW3D7P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["1 2 4\n2\n0\n3", "5 0 1\n0", "0 1 5\n3\n0\n2\n4", "-5 10 3\n1\n2"]
        if i < len(fixed):
            return fixed[i]
        a = random.randint(-1000, 1000)
        d = random.randint(-1000, 1000)
        n = random.randint(1, 20)
        q = random.randint(0, 5)
        lines = [f"{a} {d} {n}", str(q)]
        for _ in range(q):
            lines.append(str(random.randint(0, n - 1)))
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        a, d, n = map(int, lines[0].split())
        q = int(lines[1])
        out = [" ".join(str(a + d * k) for k in range(n))]
        for k in range(q):
            idx = int(lines[2 + k])
            out.append(str(a + d * idx))
        return "\n".join(out)


problem_generator = ProblemW3D7P3(test_num=10)
problem_generator.generate()
