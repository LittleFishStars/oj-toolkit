from generator import Generator
import random


class ProblemW2D2P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [1, 3, 10, 100]
        n = fixed[i] if i < len(fixed) else random.randint(1, 100)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        lines = []
        i = n
        while i:
            lines.append(str(i))
            i -= 1
        return "\n".join(lines)


problem_generator = ProblemW2D2P1(test_num=10)
problem_generator.generate()
