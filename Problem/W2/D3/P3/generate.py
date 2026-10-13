from generator import Generator
import random


class ProblemW2D3P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["5\n3\n0", "7\n0", "0", "1\n2\n3\n4\n0", "-2\n2\n0"]
        if i < len(fixed):
            return fixed[i]
        count = random.randint(1, 8)
        lines = [str(random.randint(1, 1000) * random.choice([1, -1])) for _ in range(count)]
        lines.append("0")
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        total = 0
        for line in input_data.split("\n"):
            x = int(line)
            if x == 0:
                break
            total += x
        return str(total)


problem_generator = ProblemW2D3P3(test_num=10)
problem_generator.generate()
