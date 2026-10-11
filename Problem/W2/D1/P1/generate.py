from generator import Generator
import random


class ProblemW2D1P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [5, 1, 100, 10000, 2]
        n = fixed[i] if i < len(fixed) else random.randint(1, 10000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        total = 0
        for x in range(1, n + 1):
            total += x
        return str(total)


problem_generator = ProblemW2D1P1(test_num=10)
problem_generator.generate()
