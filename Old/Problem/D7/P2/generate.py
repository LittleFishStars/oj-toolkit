from generator import Generator
import random


class D7P2(Generator):
    def generate_input(self) -> str:
        apples = [random.randint(100, 200) for _ in range(10)]
        hand_reach = random.randint(100, 120)
        return " ".join(map(str, apples)) + "\n" + str(hand_reach)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        apples = list(map(int, lines[0].split()))
        hand_reach = int(lines[1])
        total_reach = hand_reach + 30
        count = sum(1 for h in apples if h <= total_reach)
        return str(count)


problem_generator = D7P2(test_num=10)
problem_generator.generate()
