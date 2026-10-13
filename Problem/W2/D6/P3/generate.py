from generator import Generator
import random


class ProblemW2D6P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [153, 100, 9474, 7, 10, 370, 1000000]
        if i < len(fixed):
            return str(fixed[i])
        if random.random() < 0.4:
            n = random.choice([1, 5, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834])
        else:
            n = random.randint(1, 1000000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        digits = 0
        m = n
        while m:
            digits += 1
            m //= 10
        total = 0
        m = n
        while m:
            d = m % 10
            total += d ** digits
            m //= 10
        return "1" if total == n else "0"


problem_generator = ProblemW2D6P3(test_num=10)
problem_generator.generate()
