from generator import Generator
import random


class ProblemW3D5P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "100\n3\ndeposit 50\nwithdraw 200\nwithdraw 30",
            "0\n1\nwithdraw 1",
            "0\n2\ndeposit 1000000\nwithdraw 1000000",
            "7\n2\ndeposit 1\ndeposit 1",
            "1000000\n1\nwithdraw 1000000",
        ]
        if i < len(fixed):
            return fixed[i]
        balance = random.randint(0, 1000000)
        m = random.randint(1, 8)
        lines = [str(balance), str(m)]
        for _ in range(m):
            kind = random.choice(["deposit", "withdraw"])
            lines.append(f"{kind} {random.randint(1, 1000)}")
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        balance = int(lines[0])
        m = int(lines[1])
        out = []
        for k in range(m):
            kind, x = lines[2 + k].split()
            x = int(x)
            if kind == "deposit":
                balance += x
                out.append(str(balance))
            else:
                if x > balance:
                    out.append("no")
                else:
                    balance -= x
                    out.append(str(balance))
        return "\n".join(out)


problem_generator = ProblemW3D5P2(test_num=10)
problem_generator.generate()
