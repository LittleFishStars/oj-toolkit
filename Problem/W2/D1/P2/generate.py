from generator import Generator
import random


class ProblemW2D1P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [1234, 0, 9, 999999999, 10]
        n = fixed[i] if i < len(fixed) else random.randint(0, 1000000000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        total = 0
        while n:
            total += n % 10
            n //= 10
        return str(total)


problem_generator = ProblemW2D1P2(test_num=10)
problem_generator.generate()
