from generator import Generator
import random

class ProblemW1D6P4(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["800 0", "2500 1", "1000 0", "1001 0", "1000 1", "999 1"]
        if i < len(fixed):
            return fixed[i]
        w = random.choice([random.randint(1, 1000), random.randint(1001, 100000)])
        return f"{w} {random.randint(0, 1)}"

    def generate_output(self, input_data: str) -> str:
        w, u = map(int, input_data.split())
        fee = 8
        if w > 1000:
            extra_kg = (w - 1000 + 999) // 1000
            fee += extra_kg * 4
        if u == 1:
            fee += 5
        return str(fee)

problem_generator = ProblemW1D6P4(test_num=10)
problem_generator.generate()
