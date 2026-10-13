from generator import Generator
import random


class ProblemW2D4P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["2 10", "4 4", "2 2", "100 200", "990 1000"]
        if i < len(fixed):
            return fixed[i]
        a = random.randint(2, 990)
        b = random.randint(a, 1000)
        return f"{a} {b}"

    def generate_output(self, input_data: str) -> str:
        a, b = map(int, input_data.split())
        count = 0
        for n in range(a, b + 1):
            is_prime = True
            for d in range(2, n):
                if n % d == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
        return str(count)


problem_generator = ProblemW2D4P2(test_num=10)
problem_generator.generate()
