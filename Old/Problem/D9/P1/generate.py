from generator import Generator
import random


class D9P1(Generator):
    def generate_input(self) -> str:
        N = random.randint(2, 12)
        lines = [str(N)]
        for v in range(2, N + 1):
            u = random.randint(1, v - 1)
            lines.append(f"{u} {v}")
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        N = int(lines[0])
        parent = [0] * (N + 1)
        parent[1] = 0
        for i in range(1, N):
            u, v = map(int, lines[i].split())
            parent[v] = u
        out_lines = [str(parent[i]) for i in range(1, N + 1)]
        return "\n".join(out_lines)


problem_generator = D9P1(test_num=10)
problem_generator.generate()
