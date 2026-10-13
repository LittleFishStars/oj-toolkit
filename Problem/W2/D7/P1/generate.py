from generator import Generator
import random


class ProblemW2D7P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [121, 1234, 7, 0, 1000000000, 1001, 12]
        if i < len(fixed):
            return str(fixed[i])
        if random.random() < 0.4:
            half = "".join(random.choice("0123456789") for _ in range(random.randint(1, 5)))
            n = int(half + half[::-1] if random.random() < 0.5 else half + random.choice("0123456789") + half[::-1])
        else:
            n = random.randint(0, 1000000000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        s = input_data.strip()
        return "Yes" if s == s[::-1] else "No"


problem_generator = ProblemW2D7P1(test_num=10)
problem_generator.generate()
