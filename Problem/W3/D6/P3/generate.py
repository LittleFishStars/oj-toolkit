from generator import Generator
import random


class ProblemW3D6P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "2 2 2\n1 2\n3 4\n5 6\n7 8",
            "1 3 1\n1 2 3\n4\n5\n6",
            "1 1 1\n5\n7",
            "2 1 2\n1\n2\n3 4",
            "3 3 3\n1 0 0\n0 1 0\n0 0 1\n1 2 3\n4 5 6\n7 8 9",
        ]
        if i < len(fixed):
            return fixed[i]
        n = random.randint(1, 3)
        k = random.randint(1, 3)
        m = random.randint(1, 3)
        lines = [f"{n} {k} {m}"]
        for _ in range(n):
            lines.append(" ".join(str(random.randint(0, 100)) for _ in range(k)))
        for _ in range(k):
            lines.append(" ".join(str(random.randint(0, 100)) for _ in range(m)))
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        n, k, m = map(int, lines[0].split())
        a = [list(map(int, lines[1 + r].split())) for r in range(n)]
        b = [list(map(int, lines[1 + n + r].split())) for r in range(k)]
        c = []
        for r in range(n):
            row = []
            for col in range(m):
                total = 0
                for t in range(k):
                    total += a[r][t] * b[t][col]
                row.append(total)
            c.append(row)
        return "\n".join(" ".join(str(x) for x in row) for row in c)


problem_generator = ProblemW3D6P3(test_num=10)
problem_generator.generate()
