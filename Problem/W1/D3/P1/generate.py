from generator import Generator
import random

class ProblemW1D3P1(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = [17, 18, 19, 1, 80]
        age = fixed[i] if i < len(fixed) else random.randint(1, 80)
        return str(age)

    def generate_output(self, input_data: str) -> str:
        age = int(input_data)
        return "成年了" if age >= 18 else "还没成年"

problem_generator = ProblemW1D3P1(test_num=10)
problem_generator.generate()
