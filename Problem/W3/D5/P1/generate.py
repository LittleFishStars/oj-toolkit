from generator import Generator
import random


class ProblemW3D5P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["3\nadd 3 4\ndiv 7 2\nmul 2 5", "1\nsub 5 9", "2\ndiv 10 4\nadd 0 0"]
        if i < len(fixed):
            return fixed[i]
        m = random.randint(1, 8)
        lines = [str(m)]
        ops = ["add", "sub", "mul", "div"]
        for _ in range(m):
            op = random.choice(ops)
            a = random.randint(0, 1000)
            b = random.randint(1, 1000) if op == "div" else random.randint(0, 1000)
            lines.append(f"{op} {a} {b}")
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        m = int(lines[0])
        out = []
        for k in range(m):
            op, a, b = lines[1 + k].split()
            a, b = int(a), int(b)
            if op == "add":
                out.append(str(a + b))
            elif op == "sub":
                out.append(str(a - b))
            elif op == "mul":
                out.append(str(a * b))
            else:
                out.append(f"{a / b:.2f}")
        return "\n".join(out)


problem_generator = ProblemW3D5P1(test_num=10)
problem_generator.generate()
