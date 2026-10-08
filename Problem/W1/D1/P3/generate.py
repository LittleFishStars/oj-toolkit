from generator import Generator
import random

class ProblemW1D1P3(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["Xiaoming", "Python", "world"]
        name = fixed[i] if i < len(fixed) else "".join(random.choice("abcdefgh") for _ in range(random.randint(1, 10)))
        return name

    def generate_output(self, input_data: str) -> str:
        return f"你好, {input_data}!"

problem_generator = ProblemW1D1P3(test_num=10)
problem_generator.generate()
