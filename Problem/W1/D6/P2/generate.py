from generator import Generator
import random

class ProblemW1D6P2(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["hello world", "aeiou", "python", "xyz?!"]
        if i < len(fixed):
            return fixed[i]
        pool = "abcdefghijklmnop ?!123"
        return "".join(random.choice(pool) for _ in range(random.randint(1, 40)))

    def generate_output(self, input_data: str) -> str:
        s = input_data
        return f"a:{s.count('a')} e:{s.count('e')} i:{s.count('i')} o:{s.count('o')} u:{s.count('u')}"

problem_generator = ProblemW1D6P2(test_num=10)
problem_generator.generate()
