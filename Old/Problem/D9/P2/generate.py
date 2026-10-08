from generator import Generator
import random


class D9P2(Generator):
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
        children = [[] for _ in range(N + 1)]
        for i in range(1, N):
            u, v = map(int, lines[i].split())
            children[u].append(v)
        out_lines = []
        for i in range(1, N + 1):
            children[i].sort()
            if children[i]:
                out_lines.append(f"{i}: {' '.join(map(str, children[i]))}")
            else:
                out_lines.append(f"{i}:")
        return "\n".join(out_lines)


problem_generator = D9P2(test_num=10)
problem_generator.generate()
