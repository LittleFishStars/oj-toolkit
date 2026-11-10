from generator import Generator
import random


class ProblemW3D1P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [-3, 5, 12, 0, 10, -1000, 1000]
        if i < len(fixed):
            return str(fixed[i])
        return str(random.randint(-1000, 1000))

    def generate_output(self, input_data: str) -> str:
        x = int(input_data)
        if x < 0:
            return str(-x)
        if x < 10:
            return str(x * x)
        return str(x + 100)


problem_generator = ProblemW3D1P1(test_num=10)
problem_generator.generate()
