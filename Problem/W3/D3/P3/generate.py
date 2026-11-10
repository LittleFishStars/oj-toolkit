from generator import Generator
import random


class ProblemW3D3P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [7, 0, 1, 10000, 5000]
        if i < len(fixed):
            return str(fixed[i])
        return str(random.randint(0, 10000))

    def generate_output(self, input_data: str) -> str:
        return str(int(input_data) * 2)


problem_generator = ProblemW3D3P3(test_num=10)
problem_generator.generate()
