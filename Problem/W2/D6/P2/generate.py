from generator import Generator
import random


class ProblemW2D6P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["5\n88 59 72 90 45", "1\n59", "1\n60", "3\n100 100 100", "4\n0 0 0 0"]
        if i < len(fixed):
            return fixed[i]
        n = random.randint(1, 100)
        scores = [random.randint(0, 100) for _ in range(n)]
        return f"{n}\n{' '.join(str(x) for x in scores)}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        scores = list(map(int, lines[1].split()))
        highest = scores[0]
        lowest = scores[0]
        total = 0
        passed = 0
        for s in scores:
            if s > highest:
                highest = s
            if s < lowest:
                lowest = s
            total += s
            if s >= 60:
                passed += 1
        average = total / len(scores)
        return f"{highest} {lowest}\n{average:.2f}\n{passed}"


problem_generator = ProblemW2D6P2(test_num=10)
problem_generator.generate()
