from generator import Generator
import random


class ProblemW3D7P4(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "3\nadd ebook pybook 10 5 100\nadd paper novel 20 2 500\nlist",
            "4\nadd paper a 10 3 1\nsell a 1\ntotal\nlist",
            "2\nadd paper solo 7 1 1\ntotal",
            "5\nadd ebook e1 100 10 1\nadd ebook e2 100 10 1\nlist\ntotal\nlist",
        ]
        if i < len(fixed):
            return fixed[i]
        m = random.randint(2, 10)
        names = ["pybook", "novel", "math", "history", "poem", "atlas"]
        lines = []
        used = []
        for k in range(m):
            if k == 0 or random.random() < 0.45:
                kind = random.choice(["ebook", "paper"])
                name = random.choice(names) + str(k)
                used.append(name)
                price = random.randint(1, 1000)
                stock = random.randint(0, 1000)
                extra = random.randint(1, 10000)
                lines.append(f"add {kind} {name} {price} {stock} {extra}")
            elif random.random() < 0.5 and used:
                lines.append(f"sell {random.choice(used)} {random.randint(1, 500)}")
            elif random.random() < 0.5:
                lines.append("list")
            else:
                lines.append("total")
        if "list" not in lines:
            lines.append("list")
        if "total" not in lines:
            lines.append("total")
        return f"{len(lines)}\n" + "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        m = int(lines[0])
        books = {}
        out = []
        for k in range(m):
            parts = lines[1 + k].split()
            if parts[0] == "add":
                kind, name = parts[1], parts[2]
                price, stock = int(parts[3]), int(parts[4])
                books[name] = {"kind": kind, "price": price, "stock": stock}
            elif parts[0] == "sell":
                name, amount = parts[1], int(parts[2])
                if name in books:
                    books[name]["stock"] = max(0, books[name]["stock"] - amount)
            elif parts[0] == "list":
                rows = []
                for name, b in books.items():
                    value = b["price"] * b["stock"]
                    suffix = "[电子]" if b["kind"] == "ebook" else "[纸质]"
                    rows.append((name + suffix, value))
                rows.sort(key=lambda r: (-r[1], r[0]))
                for label, value in rows:
                    out.append(f"{label} {value:.1f}")
            else:
                total = 0
                for b in books.values():
                    total += b["price"] * b["stock"]
                out.append(f"{total:.1f}")
        return "\n".join(out)


problem_generator = ProblemW3D7P4(test_num=10)
problem_generator.generate()
