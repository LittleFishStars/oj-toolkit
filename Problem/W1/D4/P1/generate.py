from generator import Generator
import random

class ProblemW1D4P1(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = [95, 59, 90, 89, 80, 79, 60, 100, 0]
        s = fixed[i] if i < len(fixed) else random.randint(0, 100)
        return str(s)

    def generate_output(self, input_data: str) -> str:
        s = int(input_data)
        if s >= 90:
            return "优秀"
        elif s >= 80:
            return "良好"
        elif s >= 60:
            return "及格"
        else:
            return "不及格"

problem_generator = ProblemW1D4P1(test_num=10)
problem_generator.generate()
