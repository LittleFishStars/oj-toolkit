from generator import Generator
import random


class D6P2(Generator):
    def generate_input(self) -> str:
        tokens = []
        stack = []
        target = random.randint(5, 20)

        while len(tokens) == 0 or len(stack) != 1 or len(tokens) < target:
            if len(stack) >= 2 and random.random() < 0.55:
                b = stack.pop()
                a = stack.pop()
                available = ["+", "*"]
                if a >= b:
                    available.append("-")
                if a > 0 and b > 0 and a % b == 0:
                    available.append("/")
                op = random.choice(available)
                tokens.append(op)
                if op == "+":
                    stack.append(a + b)
                elif op == "-":
                    stack.append(a - b)
                elif op == "*":
                    stack.append(a * b)
                elif op == "/":
                    stack.append(a // b)
            else:
                x = random.randint(1, 100)
                tokens.append(str(x))
                stack.append(x)

        n = len(tokens)
        return f"{n}\n" + " ".join(tokens)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.strip().split("\n")
        tokens = lines[1].split()
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(a // b)
            else:
                stack.append(int(token))
        return str(stack[0])


problem_generator = D6P2(test_num=10)
problem_generator.generate()
