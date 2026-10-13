from generator import Generator
import random


class ProblemW2D4P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [7, 4, 2, 9973, 100000]
        n = fixed[i] if i < len(fixed) else random.randint(2, 100000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        for d in range(2, n):
            if n % d == 0:
                return "0"
        return "1"


problem_generator = ProblemW2D4P1(test_num=10)
problem_generator.generate()
