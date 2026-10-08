from generator import Generator
import random


class D7P3(Generator):
    def generate_input(self) -> str:
        all_happy = random.random() < 0.25  # ~25% chance: output 0
        days = []

        if all_happy:
            for _ in range(7):
                school = random.randint(0, 8)
                extra = random.randint(0, 8 - school)
                days.append((school, extra))
        else:
            has_unhappy = False
            for _ in range(7):
                school = random.randint(0, 8)
                extra = random.randint(0, 8)
                days.append((school, extra))
                if school + extra > 8:
                    has_unhappy = True
            if not has_unhappy:
                idx = random.randint(0, 6)
                days[idx] = (random.randint(5, 8), random.randint(4, 8))

        lines = [f"{school} {extra}" for school, extra in days]
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        max_hours = 0
        max_day = 0
        for i in range(7):
            school, extra = map(int, lines[i].split())
            total = school + extra
            if total > max_hours:
                max_hours = total
                max_day = i + 1
        if max_hours <= 8:
            return "0"
        return str(max_day)


problem_generator = D7P3(test_num=10)
problem_generator.generate()
