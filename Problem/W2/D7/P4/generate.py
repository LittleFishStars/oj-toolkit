from generator import Generator
import random


class ProblemW2D7P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["III", "IV", "MCMXCIV", "MMMCMXCIX", "I", "XL"]
        if i < len(fixed):
            return fixed[i]
        table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                 (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        m = random.randint(1, 3999)
        result = ""
        for value, symbol in table:
            while m >= value:
                result += symbol
                m -= value
        return result

    def generate_output(self, input_data: str) -> str:
        value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = input_data.strip()
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and value[s[i]] < value[s[i + 1]]:
                total -= value[s[i]]
            else:
                total += value[s[i]]
        return str(total)


problem_generator = ProblemW2D7P4(test_num=10)
problem_generator.generate()
