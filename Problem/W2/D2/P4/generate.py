from generator import Generator
import random


class ProblemW2D2P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [1, 3, 5, 20]
        n = fixed[i] if i < len(fixed) else random.randint(1, 20)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        lines = []
        i = 1
        while i <= n:
            lines.append(" " * (n - i) + "#" * (2 * i - 1))
            i += 1
        return "\n".join(lines)


problem_generator = ProblemW2D2P4(test_num=10)
problem_generator.generate()
