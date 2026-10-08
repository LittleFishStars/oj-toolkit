from generator import Generator
import random

class ProblemW1D7P4(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["5 0 0", "30 1 0", "30 0 0", "70 1 1", "6 0 0", "59 1 1", "60 0 1"]
        if i < len(fixed):
            return fixed[i]
        age = random.choice([random.randint(1, 6), random.randint(7, 59), random.randint(60, 100)])
        return f"{age} {random.randint(0, 1)} {random.randint(0, 1)}"

    def generate_output(self, input_data: str) -> str:
        age, student, member = map(int, input_data.split())
        if age < 6 or age >= 60:
            return "0"
        if student == 1:
            return "5"
        if member == 1:
            return "9"
        return "10"

problem_generator = ProblemW1D7P4(test_num=10)
problem_generator.generate()
