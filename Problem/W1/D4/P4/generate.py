from generator import Generator
import random

class ProblemW1D4P4(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = ["65 1.70", "45 1.60", "80 1.70", "90 1.75", "70 1.80", "120 1.65"]
        if i < len(fixed):
            return fixed[i]
        w = random.randint(30, 150)
        h = random.randint(120, 220) / 100
        return f"{w} {h}"

    def generate_output(self, input_data: str) -> str:
        w, h = map(float, input_data.split())
        bmi = w / (h * h)
        if bmi < 18.5:
            cat = "偏瘦"
        elif bmi < 24:
            cat = "正常"
        elif bmi < 28:
            cat = "偏胖"
        else:
            cat = "肥胖"
        return f"{bmi:.1f} {cat}"

problem_generator = ProblemW1D4P4(test_num=10)
problem_generator.generate()
