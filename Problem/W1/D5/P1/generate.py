from generator import Generator
import random

class ProblemW1D5P1(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["level", "python", "a", "aa", "ab", "aba"]
        if i < len(fixed):
            return fixed[i]
        if i % 2 == 0:  # 偶数组生成回文
            half = "".join(random.choice("abc") for _ in range(random.randint(1, 5)))
            return half + half[::-1]
        return "".join(random.choice("abcd") for _ in range(random.randint(1, 10)))

    def generate_output(self, input_data: str) -> str:
        s = input_data
        return "Yes" if s == s[::-1] else "No"

problem_generator = ProblemW1D5P1(test_num=10)
problem_generator.generate()
