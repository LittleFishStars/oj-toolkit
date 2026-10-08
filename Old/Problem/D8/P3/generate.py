from generator import Generator
import random


class D8P3(Generator):
    def generate_input(self) -> str:
        N = random.randint(2, 8)
        max_edges = N * (N - 1) // 2
        M = random.randint(1, max_edges)
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
        matrix = [[0] * M for _ in range(N)]
        for j in range(1, M + 1):
            u, v = map(int, lines[j].split())
            matrix[u - 1][j - 1] = 1
            matrix[v - 1][j - 1] = 1
        out_lines = []
        for row in matrix:
            out_lines.append(" ".join(map(str, row)))
        return "\n".join(out_lines)


problem_generator = D8P3(test_num=10)
problem_generator.generate()
