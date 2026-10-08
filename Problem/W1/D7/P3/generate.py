from generator import Generator
import random

class ProblemW1D7P3(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        pool = ["math", "english", "python", "art", "music", "pe", "history"]
        fixed = [["math english python", "python art math"], ["math english", "art music"]]
        if i < len(fixed):
            return "\n".join(fixed[i])
        a = " ".join(random.sample(pool, random.randint(1, 5)))
        b = " ".join(random.sample(pool, random.randint(1, 5)))
        return f"{a}\n{b}"

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        common = set(lines[0].split()) & set(lines[1].split())
        return " ".join(sorted(common)) if common else "None"

problem_generator = ProblemW1D7P3(test_num=10)
problem_generator.generate()
