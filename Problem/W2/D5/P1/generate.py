from generator import Generator
import random


class ProblemW2D5P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [5, 1, 10, 100, 2]
        n = fixed[i] if i < len(fixed) else random.randint(1, 100)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        squares = [x * x for x in range(1, n + 1)]
        return " ".join(str(s) for s in squares)


problem_generator = ProblemW2D5P1(test_num=10)
problem_generator.generate()
