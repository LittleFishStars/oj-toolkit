from generator import Generator
import random


class ProblemW2D4P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [1, 5, 2, 100, 50]
        n = fixed[i] if i < len(fixed) else random.randint(1, 100)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        target = int(input_data)
        count = 0
        n = 2
        while count < target:
            is_prime = True
            for d in range(2, n):
                if n % d == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
                if count == target:
                    return str(n)
            n += 1


problem_generator = ProblemW2D4P3(test_num=10)
problem_generator.generate()
