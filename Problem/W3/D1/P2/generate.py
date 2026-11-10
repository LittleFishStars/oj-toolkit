from generator import Generator
import random


class ProblemW3D1P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["1 2 3", "0", "5", "-3 3", "1000 -1000 7", ""]
        if i < len(fixed):
            return fixed[i]
        count = random.randint(0, 20)
        nums = [random.randint(-1000, 1000) for _ in range(count)]
        return " ".join(str(x) for x in nums)

    def generate_output(self, input_data: str) -> str:
        text = input_data.strip()
        if not text:
            return "0"
        nums = list(map(int, text.split()))
        total = 0
        for x in nums:
            total += x
        return str(total)


problem_generator = ProblemW3D1P2(test_num=10)
problem_generator.generate()
