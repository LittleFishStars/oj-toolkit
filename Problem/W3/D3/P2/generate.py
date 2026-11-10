from generator import Generator
import random


class ProblemW3D3P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["square 5", "circle 2", "circle 1", "square 1000", "circle 1000"]
        if i < len(fixed):
            return fixed[i]
        kind = random.choice(["square", "circle"])
        return f"{kind} {random.randint(1, 1000)}"

    def generate_output(self, input_data: str) -> str:
        kind, x = input_data.split()
        x = int(x)
        if kind == "square":
            return f"{x * x:.2f}"
        return f"{3.14 * x * x:.2f}"


problem_generator = ProblemW3D3P2(test_num=10)
problem_generator.generate()
