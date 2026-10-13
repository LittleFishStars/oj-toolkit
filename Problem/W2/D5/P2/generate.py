from generator import Generator
import random


class ProblemW2D5P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["5 2 7 8 3", "2 4 6", "-1 -2 -4", "9 11 13 15 16", "8 8 8"]
        if i < len(fixed):
            return fixed[i]
        count = random.randint(1, 19)
        nums = [random.randint(-1000, 1000) for _ in range(count)]
        nums.append(random.choice([-1000, -2, 0, 2, 4, 1000]))
        return " ".join(str(x) for x in nums)

    def generate_output(self, input_data: str) -> str:
        nums = list(map(int, input_data.split()))
        evens = [x for x in nums if x % 2 == 0]
        return " ".join(str(x) for x in evens)


problem_generator = ProblemW2D5P2(test_num=10)
problem_generator.generate()
