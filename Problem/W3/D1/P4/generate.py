from generator import Generator
import random


class ProblemW3D1P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["25 12 7 21", "9 8 7", "0", "100 10 1", "999 888 777"]
        if i < len(fixed):
            return fixed[i]
        count = random.randint(1, 20)
        nums = [random.randint(0, 1000) for _ in range(count)]
        return " ".join(str(x) for x in nums)

    def generate_output(self, input_data: str) -> str:
        nums = list(map(int, input_data.split()))

        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        result = sorted(nums, key=lambda x: (digit_sum(x), x))
        return " ".join(str(x) for x in result)


problem_generator = ProblemW3D1P4(test_num=10)
problem_generator.generate()
