from generator import Generator
import random


class D9P4(Generator):
    def generate_input(self) -> str:
        N = random.randint(2, 15)
        lines = [str(N)]
        for v in range(2, N + 1):
            u = random.randint(1, v - 1)
            lines.append(f"{u} {v}")
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        N = int(lines[0])
        has_child = [False] * (N + 1)
        for i in range(1, N):
            u, v = map(int, lines[i].split())
            has_child[u] = True
        leaf_count = 0
        for i in range(1, N + 1):
            if not has_child[i]:
                leaf_count += 1
        return str(leaf_count)


problem_generator = D9P4(test_num=10)
problem_generator.generate()
