from generator import Generator
import random


class ProblemW2D1P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [1, 3, 9, 2]
        n = fixed[i] if i < len(fixed) else random.randint(1, 9)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        lines = []
        for i in range(1, n + 1):
            row = []
            for j in range(1, i + 1):
                row.append(f"{i}*{j}={i * j}")
            lines.append(" ".join(row))
        return "\n".join(lines)


problem_generator = ProblemW2D1P4(test_num=10)
problem_generator.generate()
