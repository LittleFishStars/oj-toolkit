from generator import Generator
import random


class ProblemW2D1P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [5, 0, 1, 12, 10]
        n = fixed[i] if i < len(fixed) else random.randint(0, 12)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        result = 1
        for x in range(1, n + 1):
            result *= x
        return str(result)


problem_generator = ProblemW2D1P3(test_num=10)
problem_generator.generate()
