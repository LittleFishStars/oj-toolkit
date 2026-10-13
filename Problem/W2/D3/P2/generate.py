from generator import Generator
import random


class ProblemW2D3P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [9, 17, 2, 4, 100000]
        n = fixed[i] if i < len(fixed) else random.randint(2, 100000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data)
        answer = n
        for d in range(2, n + 1):
            if n % d == 0:
                answer = d
                break
        return str(answer)


problem_generator = ProblemW2D3P2(test_num=10)
problem_generator.generate()
