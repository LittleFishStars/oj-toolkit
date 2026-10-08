from generator import Generator
import random

NAMES = [
    "Alice", "Bob", "Cathy", "David", "Eve", "Frank", "Grace",
    "Henry", "Ivy", "Jack", "Kate", "Leo", "Mary", "Nick",
    "Olivia", "Paul", "Queenie", "Rose", "Sam", "Tom",
    "Uma", "Victor", "Wendy", "Xavier", "Yuki", "Zack",
]

PREFIX_NAMES = [
    "Al", "Ali", "Alice", "Alex", "Ann", "Anna",
    "Bob", "Ben", "Bill",
    "Cathy", "Carl", "Cate",
    "David", "Dan", "Dave",
    "Eve", "Ed", "Emma",
    "Frank", "Fred",
    "Grace", "Gray",
    "Henry", "Hank",
    "Ivy", "Ian",
    "Jack", "Jane", "Jim",
    "Kate", "Ken",
    "Leo", "Lee", "Liam",
    "Mary", "May", "Mike",
    "Nick", "Nina",
    "Olivia", "Oscar",
    "Paul", "Pat",
    "Queenie",
    "Rose", "Roy", "Ray",
    "Sam", "Sue",
    "Tom", "Tim",
    "Uma",
    "Victor", "Vic",
    "Wendy", "Will",
    "Xavier",
    "Yuki",
    "Zack", "Zoe",
]

def shuffle(lines):
    random.shuffle(lines)
    return lines

class D5P2(Generator):
    def generate_input(self) -> str:
        n = random.randint(3, 20)
        strategy = random.randint(1, 5)
        lines = []

        if strategy == 1:
            names = random.sample(NAMES, min(n, len(NAMES)))
            for name in names:
                lines.append(f"{name} {random.randint(1, 100)}")

        elif strategy == 2:
            name = random.choice(NAMES)
            for _ in range(n):
                lines.append(f"{name} {random.randint(1, 100)}")

        elif strategy == 3:
            name = random.choice(NAMES)
            age = random.randint(1, 100)
            for _ in range(n):
                lines.append(f"{name} {age}")

        elif strategy == 4:
            prefix_groups = [
                ["Al", "Ali", "Alice", "Alex"],
                ["Ann", "Anna"],
                ["Ben", "Bill", "Bob"],
                ["Carl", "Cate", "Cathy"],
                ["Dan", "Dave", "David"],
                ["Ed", "Emma", "Eve"],
                ["Frank", "Fred"],
                ["Grace", "Gray"],
                ["Hank", "Henry"],
                ["Ian", "Ivy"],
                ["Jack", "Jane"],
                ["Kate", "Ken"],
                ["Lee", "Leo", "Liam"],
                ["Mary", "May", "Mike"],
                ["Nick", "Nina"],
                ["Oscar", "Olivia"],
                ["Pat", "Paul"],
                ["Ray", "Rose", "Roy"],
                ["Sam", "Sue"],
                ["Tim", "Tom"],
                ["Vic", "Victor"],
                ["Will", "Wendy"],
                ["Zack", "Zoe"],
            ]
            group = random.choice(prefix_groups)
            for name in group:
                lines.append(f"{name} {random.randint(1, 100)}")
            while len(lines) < n:
                extra = random.choice(NAMES)
                lines.append(f"{extra} {random.randint(1, 100)}")

        else:
            for _ in range(n):
                name = random.choice(PREFIX_NAMES)
                age = random.randint(1, 100)
                lines.append(f"{name} {age}")

        shuffle(lines)
        return f"{n}\n" + "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        n = int(lines[0])
        entries = []
        for i in range(1, n + 1):
            name, age = lines[i].split()
            entries.append((name, int(age), i))
        entries.sort(key=lambda x: (x[0], x[1], x[2]))
        return "\n".join(f"{name} {age}" for name, age, _ in entries)

problem_generator = D5P2(test_num=20)
problem_generator.generate()
