from generator import Generator
import random

class ProblemW1D3P4(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["3 + 5", "7 / 2", "5 / 0", "10 * 3", "9 - 12", "4 / 0"]
        if i < len(fixed):
            return fixed[i]
        a = random.randint(0, 100)
        b = random.choice([0, 0, random.randint(1, 100)])
        op = random.choice("+-*/")
        return f"{a} {op} {b}"

    def generate_output(self, input_data: str) -> str:
        a, op, b = input_data.split()
        a, b = int(a), int(b)
        if op == "+":
            return str(a + b)
        if op == "-":
            return str(a - b)
        if op == "*":
            return str(a * b)
        if b == 0:
            return "Error"
        return f"{a / b:.2f}"

problem_generator = ProblemW1D3P4(test_num=10)
problem_generator.generate()
