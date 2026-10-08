from generator import Generator
import random

class ProblemW1D5P4(Generator):
    def generate_input(self) -> str:
        i = getattr(self, "_i", 0)
        self._i = i + 1
        names = ["Alice", "Bob", "Cindy", "David", "Eve", "Frank", "Grace", "Tom"]
        if i == 0:
            book = {"Alice": "13800000001", "Bob": "13800000002", "Cindy": "13800000003"}
            queries = ["Bob", "David"]
        else:
            k = random.randint(1, 8)
            book = {}
            for _ in range(k):
                name = random.choice(names)
                book[name] = "13" + str(random.randint(100000000, 999999999))
            queries = [random.choice(names) for _ in range(random.randint(1, 5))]
        lines = [str(len(book))] + [f"{k} {v}" for k, v in book.items()]
        lines.append(str(len(queries)))
        lines.extend(queries)
        return "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        n = int(lines[0])
        book = {}
        for j in range(1, n + 1):
            name, phone = lines[j].split()
            book[name] = phone
        m = int(lines[n + 1])
        out = []
        for j in range(n + 2, n + 2 + m):
            q = lines[j]
            out.append(book.get(q, "Not Found"))
        return "\n".join(out)

problem_generator = ProblemW1D5P4(test_num=10)
problem_generator.generate()
