from generator import Generator
import random


class ProblemW3D3P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["3 r 3 4 s 5 t 6 8", "2 s 1 t 1 2", "1 s 1000", "1 t 1000 1000", "3 r 1 1 r 2 2 s 3"]
        if i < len(fixed):
            return fixed[i]
        count = random.randint(1, 6)
        parts = [str(count)]
        for _ in range(count):
            kind = random.choice(["r", "s", "t"])
            if kind == "r":
                parts += ["r", str(random.randint(1, 1000)), str(random.randint(1, 1000))]
            elif kind == "s":
                parts += ["s", str(random.randint(1, 1000))]
            else:
                parts += ["t", str(random.randint(1, 1000)), str(random.randint(1, 1000))]
        return " ".join(parts)

    def generate_output(self, input_data: str) -> str:
        tokens = input_data.split()
        n = int(tokens[0])
        pos = 1
        lines = []
        for _ in range(n):
            kind = tokens[pos]
            pos += 1
            if kind == "r":
                a, b = int(tokens[pos]), int(tokens[pos + 1])
                pos += 2
                lines.append(f"rect {a * b:.1f}")
            elif kind == "s":
                s = int(tokens[pos])
                pos += 1
                lines.append(f"square {s * s:.1f}")
            else:
                b, h = int(tokens[pos]), int(tokens[pos + 1])
                pos += 2
                lines.append(f"triangle {b * h / 2:.1f}")
        return "\n".join(lines)


problem_generator = ProblemW3D3P4(test_num=10)
problem_generator.generate()
