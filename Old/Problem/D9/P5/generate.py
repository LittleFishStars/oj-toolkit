from generator import Generator
import random


class D9P5(Generator):
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

        size = [1] * (N + 1)

        # Post-order traversal with explicit stack
        order = []
        stack = [1]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in children[u]:
                stack.append(v)

        for u in reversed(order):
            for v in children[u]:
                size[u] += size[v]

        out_lines = [str(size[i]) for i in range(1, N + 1)]
        return "\n".join(out_lines)


problem_generator = D9P5(test_num=10)
problem_generator.generate()
