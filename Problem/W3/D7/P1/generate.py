from generator import Generator
import random


class ProblemW3D7P1(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = ["2+3*4", "(2+3)*4", "10/4", "1", "100*100-1", "((1+2)*(3+4))"]
        if i < len(fixed):
            return fixed[i]

        def build(depth=0):
            parts = []
            for _ in range(random.randint(1, 3)):
                if depth < 2 and random.random() < 0.35:
                    parts.append("(" + build(depth + 1) + ")")
                else:
                    parts.append(str(random.randint(0, 20)))
                if random.random() < 0.7:
                    parts.append(random.choice("+-*/"))
            text = "".join(parts)
            while text and text[-1] in "+-*/":
                text = text[:-1]
            return text if text else "1"

        return build()

    def generate_output(self, input_data: str) -> str:
        expr = input_data.strip()
        # 调度场算法转后缀，再求值（整数除法向下取整）
        prec = {"+": 1, "-": 1, "*": 2, "/": 2}
        output = []
        stack = []
        num = ""
        for ch in expr:
            if ch.isdigit():
                num += ch
                continue
            if num:
                output.append(num)
                num = ""
            if ch in prec:
                while stack and stack[-1] != "(" and prec[stack[-1]] >= prec[ch]:
                    output.append(stack.pop())
                stack.append(ch)
            elif ch == "(":
                stack.append(ch)
            else:
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()
        if num:
            output.append(num)
        while stack:
            output.append(stack.pop())

        values = []
        for token in output:
            if token not in prec:
                values.append(int(token))
            else:
                b = values.pop()
                a = values.pop()
                if token == "+":
                    values.append(a + b)
                elif token == "-":
                    values.append(a - b)
                elif token == "*":
                    values.append(a * b)
                else:
                    values.append(a // b if b != 0 else 0)
        return str(values[-1])


problem_generator = ProblemW3D7P1(test_num=10)
problem_generator.generate()
