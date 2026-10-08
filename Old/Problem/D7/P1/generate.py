from generator import Generator
import random


class D7P1(Generator):
    def generate_input(self) -> str:
        L = random.randint(50, 500)
        M = random.randint(3, 20)
        regions = []
        for _ in range(M):
            u = random.randint(0, L)
            v = random.randint(u, L)
            regions.append((u, v))

        lines = [f"{L} {M}"]
        for u, v in regions:
            lines.append(f"{u} {v}")
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        L, M = map(int, lines[0].split())
        trees = [1] * (L + 1)  # 1 means tree exists
        for i in range(1, M + 1):
            u, v = map(int, lines[i].split())
            for j in range(u, v + 1):
                trees[j] = 0
        return str(sum(trees))


problem_generator = D7P1(test_num=10)
problem_generator.generate()
