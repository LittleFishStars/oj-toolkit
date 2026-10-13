from generator import Generator
import random


class ProblemW2D3P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "5\n3 7 1 9 7\n7",
            "5\n3 7 1 9 7\n5",
            "1\n42\n42",
            "1\n8\n9",
            "4\n1 1 1 1\n1",
        ]
        if i < len(fixed):
            return fixed[i]
        n = random.randint(1, 100)
        nums = [random.randint(-1000, 1000) for _ in range(n)]
        if random.random() < 0.7:
            x = random.choice(nums)
        else:
            x = random.randint(1001, 2000)
        return f"{n}\n{' '.join(str(v) for v in nums)}\n{x}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        x = int(lines[2])
        position = -1
        for i in range(n):
            if nums[i] == x:
                position = i + 1
                break
        return str(position)


problem_generator = ProblemW2D3P4(test_num=10)
problem_generator.generate()
