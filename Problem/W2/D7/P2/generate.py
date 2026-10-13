from generator import Generator
import random


class ProblemW2D7P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "3\ntom 90\namy 70\nbob 80",
            "1\nzoe 60",
            "2\nann 100\nben 100",
            "4\na 59\nb 60\nc 61\nd 0",
            "3\nli 0\nwu 0\nxu 0",
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
        names = []
        scores = []
        for k in range(n):
            name, score = lines[1 + k].split()
            names.append(name)
            scores.append(int(score))

        best = 0
        for k in range(n):
            if scores[k] > scores[best]:
                best = k

        total = 0
        for s in scores:
            total += s
        average = total / n

        above = 0
        for s in scores:
            if s > average:
                above += 1

        return f"{names[best]}\n{average:.2f}\n{above}"


problem_generator = ProblemW2D7P2(test_num=10)
problem_generator.generate()
