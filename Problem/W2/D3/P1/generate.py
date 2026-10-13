from generator import Generator
import random


class ProblemW2D3P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [10, 1, 100, 9999, 2]
        n = fixed[i] if i < len(fixed) else random.randint(1, 10000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        total = 0
        for x in range(1, n + 1):
            if x % 2 == 0:
                continue
            total += x
        return str(total)


problem_generator = ProblemW2D3P1(test_num=10)
problem_generator.generate()
