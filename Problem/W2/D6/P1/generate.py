from generator import Generator
import random


class ProblemW2D6P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["5\n-1 0 3 0 7", "1\n0", "1\n-5", "3\n1 2 3", "6\n0 0 0 0 0 0"]
        if i < len(fixed):
            return fixed[i]
        n = random.randint(1, 100)
        nums = [random.choice([0, random.randint(-1000, 1000)]) for _ in range(n)]
        return f"{n}\n{' '.join(str(x) for x in nums)}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        nums = list(map(int, lines[1].split()))
        positive = 0
        negative = 0
        zero = 0
        for x in nums:
            if x > 0:
                positive += 1
            elif x < 0:
                negative += 1
            else:
                zero += 1
        return f"{positive} {negative} {zero}"


problem_generator = ProblemW2D6P1(test_num=10)
problem_generator.generate()
