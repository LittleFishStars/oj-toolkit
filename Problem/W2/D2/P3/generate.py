from generator import Generator
import random


class ProblemW2D2P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [1, 2, 3, 6, 30]
        n = fixed[i] if i < len(fixed) else random.randint(1, 30)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        lines = []
        a, b = 1, 1
        count = 0
        while count < n:
            lines.append(str(a))
            nxt = a + b
            a = b
            b = nxt
            count += 1
        return "\n".join(lines)


problem_generator = ProblemW2D2P3(test_num=10)
problem_generator.generate()
