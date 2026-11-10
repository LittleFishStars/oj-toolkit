from generator import Generator
import random


class ProblemW3D1P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["1 2 3 4", "5", "0", "-2 -3", "10 11"]
        if i < len(fixed):
            return fixed[i]
        count = random.randint(1, 20)
        nums = [random.randint(-1000, 1000) for _ in range(count)]
        return " ".join(str(x) for x in nums)

    def generate_output(self, input_data: str) -> str:
        nums = list(map(int, input_data.split()))
        result = [x * x if x % 2 == 0 else x * 3 + 1 for x in nums]
        return " ".join(str(x) for x in result)


problem_generator = ProblemW3D1P3(test_num=10)
problem_generator.generate()
