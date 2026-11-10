from generator import Generator
import random


class ProblemW3D6P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "3\ntom 90\namy 70\nbob 50",
            "1\nzoe 59",
            "2\na 60\nb 60",
            "3\na 0\nb 100\nc 0",
            "4\nw 61\nx 62\ny 63\nz 64",
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
        names, scores = [], []
        for k in range(n):
            name, score = lines[1 + k].split()
            names.append(name)
            scores.append(int(score))
        average = sum(scores) / n
        best = 0
        for k in range(n):
            if scores[k] > scores[best]:
                best = k
        passed = 0
        for s in scores:
            if s >= 60:
                passed += 1
        rate = passed / n * 100
        return f"{n} {average:.2f}\n{names[best]}\n{rate:.1f}%"


problem_generator = ProblemW3D6P1(test_num=10)
problem_generator.generate()
