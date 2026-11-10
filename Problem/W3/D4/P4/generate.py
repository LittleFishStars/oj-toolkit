from generator import Generator
import random


class ProblemW3D4P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "2\n1 6\n3 * 5",
            "2\n3 - 5\n8 / 2",
            "1\n0 0",
            "3\n7 7\n14 + 14\n1 / 1",
            "2\n10 * 10\n20 - 13",
        ]
        if i < len(fixed):
            return fixed[i]
        m = random.randint(1, 8)
        lines = [str(m)]
        ops = ["+", "-", "*", "/"]
        for _ in range(m):
            a = random.randint(0, 1000)
            op = random.choice(ops)
            if op == "/":
                b = random.choice([1, 2, 3, 4, 5, 6, 8, 9])
            else:
                b = random.randint(0, 1000)
            lines.append(f"{a} {op} {b}")
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        m = int(lines[0])
        out = []
        for k in range(m):
            parts = lines[1 + k].split()
            a = int(parts[0]) % 7
            if len(parts) == 2:
                b = int(parts[1]) % 7
                out.append(f"[{(a + b) % 7}]")
            else:
                op = parts[1]
                b = int(parts[2]) % 7
                if op == "+":
                    out.append(f"[{(a + b) % 7}]")
                elif op == "-":
                    out.append(f"[{(a - b) % 7}]")
                elif op == "*":
                    out.append(f"[{(a * b) % 7}]")
                else:
                    out.append(f"[{(a * pow(b, 5, 7)) % 7}]")
        return "\n".join(out)


problem_generator = ProblemW3D4P4(test_num=10)
problem_generator.generate()
