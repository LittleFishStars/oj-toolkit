from generator import Generator
import random

class ProblemW1D5P2(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["5 -3 0 8 -1 0 5", "7 7 7", "3 1 2"]
        if i < len(fixed):
            return fixed[i]
        k = random.randint(1, 20)
        nums = [random.randint(-1000, 1000) for _ in range(k)]
        return " ".join(map(str, nums))

    def generate_output(self, input_data: str) -> str:
        nums = list(map(int, input_data.split()))
        return " ".join(map(str, sorted(set(nums))))

problem_generator = ProblemW1D5P2(test_num=10)
problem_generator.generate()
