from generator import Generator
import random


class ProblemW2D6P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [3524, 6174, 1000, 9998, 1234, 2111]
        if i < len(fixed):
            return str(fixed[i])
        while True:
            n = random.randint(1000, 9999)
            digits = [n // 1000, n // 100 % 10, n // 10 % 10, n % 10]
            if len(set(digits)) > 1:
                return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        steps = 0
        while n != 6174:
            digits = sorted([n // 1000, n // 100 % 10, n // 10 % 10, n % 10])
            big = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0]
            small = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
            n = big - small
            steps += 1
        return str(steps)


problem_generator = ProblemW2D6P4(test_num=10)
problem_generator.generate()
