from generator import Generator
import random

NAMES = [
    "Alice", "Bob", "Cathy", "David", "Eve", "Frank", "Grace",
    "Henry", "Ivy", "Jack", "Kate", "Leo", "Mary", "Nick",
    "Olivia", "Paul", "Queenie", "Rose", "Sam", "Tom",
    "Uma", "Victor", "Wendy", "Xavier", "Yuki", "Zack",
]

class D5P1(Generator):
    def generate_input(self) -> str:
        n = random.randint(2, 20)
        lines = []
        for _ in range(n):
            name = random.choice(NAMES)
            age = random.randint(1, 100)
            lines.append(f"{name} {age}")
        return f"{n}\n" + "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        n = int(lines[0])
        entries = []
        for i in range(1, n + 1):
            name, age = lines[i].split()
            entries.append((int(age), i, name))
        entries.sort()
        return "\n".join(f"{name} {age}" for age, _, name in entries)

problem_generator = D5P1(test_num=10)
problem_generator.generate()
