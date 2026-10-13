from generator import Generator
import random


class ProblemW2D5P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [3, 1, 5, 20, 2]
        n = fixed[i] if i < len(fixed) else random.randint(1, 20)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        squares = {x: x * x for x in range(1, n + 1)}
        return " ".join(f"{x}:{squares[x]}" for x in range(1, n + 1))


problem_generator = ProblemW2D5P3(test_num=10)
problem_generator.generate()
