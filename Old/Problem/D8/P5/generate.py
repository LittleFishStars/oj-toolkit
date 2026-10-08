from generator import Generator
import random


class D8P5(Generator):
    def generate_input(self) -> str:
        N = random.randint(1, 10)
        max_edges = N * (N - 1) // 2
        M = random.randint(0, max_edges)
        edges_set = set()
        while len(edges_set) < M:
            u = random.randint(1, N)
            v = random.randint(1, N)
            if u != v:
                edge = (min(u, v), max(u, v))
                edges_set.add(edge)
        edges = list(edges_set)

        lines = [f"{N} {M}"]
        for u, v in edges:
            lines.append(f"{u} {v}")
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        N, M = map(int, lines[0].split())
        degree = [0] * N
        for i in range(1, M + 1):
            u, v = map(int, lines[i].split())
            degree[u - 1] += 1
            degree[v - 1] += 1
        return "\n".join(map(str, degree))


problem_generator = D8P5(test_num=10)
problem_generator.generate()
