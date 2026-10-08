from generator import Generator
import random


class D6P1(Generator):
    def generate_input(self) -> str:
        n = random.randint(5, 50)
        lines = []
        stack = []  # shadow stack to ensure some empty-stack edge cases
        for _ in range(n):
            if not stack:
                # Empty stack: push with 70% chance, pop/top with 30%
                if random.random() < 0.7:
                    x = random.randint(1, 1000)
                    lines.append(f"1 {x}")
                    stack.append(x)
                else:
                    op = random.choice(["2", "3", "4"])
                    lines.append(op)
                    if op == "2":
                        pass  # stays empty
                    elif op == "3":
                        pass  # stays empty
                    # op == "4": stays empty
            else:
                r = random.random()
                if r < 0.4:
                    x = random.randint(1, 1000)
                    lines.append(f"1 {x}")
                    stack.append(x)
                elif r < 0.65:
                    lines.append("2")
                    stack.pop()
                elif r < 0.85:
                    lines.append("3")
                else:
                    lines.append("4")
        return f"{n}\n" + "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        n = int(lines[0])
        stack = []
        output = []
        for i in range(1, n + 1):
            parts = lines[i].split()
            op = int(parts[0])
            if op == 1:
                stack.append(int(parts[1]))
            elif op == 2:
                if stack:
                    output.append(str(stack.pop()))
                else:
                    output.append("Empty")
            elif op == 3:
                if stack:
                    output.append(str(stack[-1]))
                else:
                    output.append("Empty")
            elif op == 4:
                output.append(str(len(stack)))
        return "\n".join(output)


problem_generator = D6P1(test_num=10)
problem_generator.generate()
