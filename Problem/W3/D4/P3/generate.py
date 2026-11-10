from generator import Generator
import random


class ProblemW3D4P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "3\ntom 90\namy 95\nbob 60",
            "1\nzoe 100",
            "2\namy 80\nbob 80",
            "4\nd 50\nc 50\nb 50\na 50",
            "3\nx 0\ny 100\nz 50",
        ]
        if i < len(fixed):
            return fixed[i]
        n = random.randint(1, 100)
        rows = []
        for _ in range(n):
            name = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(random.randint(1, 10)))
            rows.append(f"{name} {random.randint(0, 100)}")
        return f"{n}\n" + "\n".join(rows)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        n = int(lines[0])
        rows = []
        for k in range(n):
            name, score = lines[1 + k].split()
            rows.append((int(score), name))
        rows.sort()
        return "\n".join(f"{name} {score}" for score, name in rows)


problem_generator = ProblemW3D4P3(test_num=10)
problem_generator.generate()
