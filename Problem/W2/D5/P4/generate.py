from generator import Generator
import random


class ProblemW2D5P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [3, 1, 4, 20, 2]
        n = fixed[i] if i < len(fixed) else random.randint(1, 20)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        terms = [f"+x^{k}/{k}" if k % 2 else f"-x^{k}/{k}" for k in range(1, n + 1)]
        return "".join(terms)


problem_generator = ProblemW2D5P4(test_num=10)
problem_generator.generate()
