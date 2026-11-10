from generator import Generator
import random


class ProblemW3D6P4(Generator):
    def generate_input(self) -> str:
        deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        i = self._i
        fixed = ["K 3 A 10 2", "A", "2 3 4", "A K Q J 10", "5 4 3 2"]
        if i < len(fixed):
            return fixed[i]
        count = random.randint(1, 13)
        cards = random.sample(deck, count)
        return " ".join(cards)

    def generate_output(self, input_data: str) -> str:
        order = {c: idx for idx, c in enumerate(
            ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])}
        cards = input_data.split()
        cards.sort(key=lambda c: order[c])
        return " ".join(cards)


problem_generator = ProblemW3D6P4(test_num=10)
problem_generator.generate()
