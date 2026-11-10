from generator import Generator
import random


class ProblemW3D2P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["amy 85", "bob 59", "tom 100", "zoe 0", "li 90", "wu 89"]
        if i < len(fixed):
            return fixed[i]
        name = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(random.randint(1, 10)))
        return f"{name} {random.randint(0, 100)}"

    def generate_output(self, input_data: str) -> str:
        name, score = input_data.split()
        score = int(score)
        if score >= 90:
            level = "A"
        elif score >= 80:
            level = "B"
        elif score >= 70:
            level = "C"
        elif score >= 60:
            level = "D"
        else:
            level = "E"
        return f"{name}:{score} 等级{level}"


problem_generator = ProblemW3D2P2(test_num=10)
problem_generator.generate()
