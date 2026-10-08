from generator import Generator
import random

class ProblemW1D5P3(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        fixed = [4, 13, 7, 10, 1, 0, 12, 3, 2]
        m = fixed[i] if i < len(fixed) else random.randint(0, 13)
        return str(m)

    def generate_output(self, input_data: str) -> str:
        m = int(input_data)
        if m in (3, 4, 5):
            return "春天"
        elif m in (6, 7, 8):
            return "夏天"
        elif m in (9, 10, 11):
            return "秋天"
        elif m in (12, 1, 2):
            return "冬天"
        else:
            return "无效月份"

problem_generator = ProblemW1D5P3(test_num=10)
problem_generator.generate()
