from generator import Generator
import random

class D5P3(Generator):
    def generate_input(self) -> str:
        n = random.randint(100, 1000)
        nums = [random.randint(1, 1000) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, nums))}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        nums = list(map(int, lines[1].split()))
        odds = sorted([x for x in nums if x % 2 == 1])
        evens = sorted([x for x in nums if x % 2 == 0], reverse=True)
        return " ".join(map(str, odds)) + "\n" + " ".join(map(str, evens))

problem_generator = D5P3(test_num=10)
problem_generator.generate()
