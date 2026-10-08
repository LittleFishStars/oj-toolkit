from generator import Generator
import random

class ProblemW1D6P1(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["0 1", "2 2", "1 0", "2 0", "0 2", "1 2"]
        if i < len(fixed):
            return fixed[i]
        return f"{random.randint(0, 2)} {random.randint(0, 2)}"

    def generate_output(self, input_data: str) -> str:
        a, b = map(int, input_data.split())
        if a == b:
            return "Draw"
        win = {(0, 1), (1, 2), (2, 0)}
        return "Player 1 wins" if (a, b) in win else "Player 2 wins"

problem_generator = ProblemW1D6P1(test_num=10)
problem_generator.generate()
