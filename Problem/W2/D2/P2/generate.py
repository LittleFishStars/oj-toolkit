from generator import Generator
import random


class ProblemW2D2P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [1234, 1200, 0, 7, 1000000000]
        n = fixed[i] if i < len(fixed) else random.randint(0, 1000000000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        result = 0
        while n:
            result = result * 10 + n % 10
            n //= 10
        return str(result)


problem_generator = ProblemW2D2P2(test_num=10)
problem_generator.generate()
