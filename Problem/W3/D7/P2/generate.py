from generator import Generator
import random


class ProblemW3D7P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "3\nadd food apple 10 5 30\nadd tool hammer 100 2 1\nreport",
            "4\nadd tool saw 10 3 0\nsell saw 2\nadd food milk 5 4 7\nreport",
            "2\nadd tool a 1 1 0\nreport",
            "5\nadd food f 100 10 1\nadd food g 100 10 1\nreport\nsell f 100\nreport",
        ]
        if i < len(fixed):
            return fixed[i]
        m = random.randint(2, 10)
        names = ["apple", "milk", "saw", "hammer", "bread", "nails", "juice", "rope"]
        lines = []
        used = set()
        for k in range(m):
            if k == 0 or random.random() < 0.5:
                kind = random.choice(["food", "tool"])
                name = random.choice(names)
                while name in used:
                    name = name + "x"
                used.add(name)
                price = random.randint(1, 1000)
                qty = random.randint(0, 1000)
                extra = random.randint(1, 365) if kind == "food" else random.randint(0, 1)
                lines.append(f"add {kind} {name} {price} {qty} {extra}")
            elif random.random() < 0.6:
                lines.append(f"sell {random.choice(list(used))} {random.randint(1, 1000)}")
            else:
                lines.append("report")
        if "report" not in lines:
            lines.append("report")
        return f"{len(lines)}\n" + "\n".join(lines)

    def generate_output(self, input_data: str) -> str:
        lines = input_data.split("\n")
        m = int(lines[0])
        items = {}
        out = []
        for k in range(m):
            parts = lines[1 + k].split()
            if parts[0] == "add":
                kind, name, price, qty, extra = parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5])
                items[name] = {"kind": kind, "price": price, "qty": qty, "extra": extra}
            elif parts[0] == "sell":
                name, amount = parts[1], int(parts[2])
                if name in items:
                    items[name]["qty"] = max(0, items[name]["qty"] - amount)
            else:
                rows = []
                for name, it in items.items():
                    value = it["price"] * it["qty"]
                    if it["kind"] == "food":
                        value *= 0.9
                    elif it["extra"] == 1:
                        value *= 1.1
                    rows.append((name, value))
                rows.sort(key=lambda r: (-r[1], r[0]))
                for name, value in rows:
                    out.append(f"{name} {value:.1f}")
        return "\n".join(out)


problem_generator = ProblemW3D7P2(test_num=10)
problem_generator.generate()
