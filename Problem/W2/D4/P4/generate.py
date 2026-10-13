from generator import Generator
import random


class ProblemW2D4P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [12, 97, 100, 2, 65536]
        n = fixed[i] if i < len(fixed) else random.randint(2, 100000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        parts = []
        d = 2
        while n > 1:
            while n % d == 0:
                parts.append(str(d))
                n //= d
            d += 1
        return "*".join(parts)


problem_generator = ProblemW2D4P4(test_num=10)
problem_generator.generate()
