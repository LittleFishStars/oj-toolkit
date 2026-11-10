from generator import Generator
import random


class ProblemW3D5P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["3 rect 3 4 square 5 circle 1", "1 square 1", "1 circle 1000", "2 rect 1 1 rect 2 2"]
        if i < len(fixed):
            return fixed[i]
        count = random.randint(1, 5)
        parts = [str(count)]
        for _ in range(count):
            kind = random.choice(["rect", "square", "circle"])
            if kind == "rect":
                parts += ["rect", str(random.randint(1, 1000)), str(random.randint(1, 1000))]
            elif kind == "square":
                parts += ["square", str(random.randint(1, 1000))]
            else:
                parts += ["circle", str(random.randint(1, 1000))]
        return " ".join(parts)

    def generate_output(self, input_data: str) -> str:
        tokens = input_data.split()
        n = int(tokens[0])
        pos = 1
        total = 0.0
        for _ in range(n):
            kind = tokens[pos]
            pos += 1
            if kind == "rect":
                a, b = int(tokens[pos]), int(tokens[pos + 1])
                pos += 2
                total += a * b
            elif kind == "square":
                s = int(tokens[pos])
                pos += 1
                total += s * s
            else:
                r = int(tokens[pos])
                pos += 1
                total += 3.14 * r * r
        return f"{total:.2f}"


problem_generator = ProblemW3D5P4(test_num=10)
problem_generator.generate()
