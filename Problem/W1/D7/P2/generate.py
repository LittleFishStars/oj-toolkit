from generator import Generator
import random

class ProblemW1D7P2(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["3 7 5", "8", "-5 0 5", "10 10 10"]
        if i < len(fixed):
            return fixed[i]
        k = random.randint(1, 20)
        nums = [random.randint(-1000, 1000) for _ in range(k)]
        return " ".join(map(str, nums))

    def generate_output(self, input_data: str) -> str:
        nums = list(map(int, input_data.split()))
        return f"{max(nums)}\n{min(nums)}\n{sum(nums) / len(nums):.2f}"

problem_generator = ProblemW1D7P2(test_num=10)
problem_generator.generate()
