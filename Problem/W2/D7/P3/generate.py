from generator import Generator
import random


class ProblemW2D7P3(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["Hello World 123!", "abc", "ABC123", "Aa1!", "Zz 09 ?!"]
        if i < len(fixed):
            return fixed[i]
        pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789     !?.,-_"
        length = random.randint(1, 100)
        text = "".join(random.choice(pool) for _ in range(length))
        while text[0] == " ":
            text = random.choice("abcXYZ019") + text[1:]
        while text[-1] == " ":
            text = text[:-1] + random.choice("abcXYZ019")
        return text

    def generate_output(self, input_data: str) -> str:
        upper = 0
        lower = 0
        digit = 0
        other = 0
        for ch in input_data:
            if "A" <= ch <= "Z":
                upper += 1
            elif "a" <= ch <= "z":
                lower += 1
            elif "0" <= ch <= "9":
                digit += 1
            else:
                other += 1
        return f"{upper} {lower} {digit} {other}"


problem_generator = ProblemW2D7P3(test_num=10)
problem_generator.generate()
