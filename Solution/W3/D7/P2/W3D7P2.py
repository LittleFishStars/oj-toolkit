class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def value(self):
        return self.price * self.qty

    def __str__(self):
        return self.name


class Food(Item):
    def __init__(self, name, price, qty, days):
        super().__init__(name, price, qty)
        self.days = days

    def value(self):
        return super().value() * 0.9


class Tool(Item):
    def __init__(self, name, price, qty, imported):
        super().__init__(name, price, qty)
        self.imported = imported

    def value(self):
        if self.imported == 1:
            return super().value() * 1.1
        return super().value()


m = int(input())
items = {}
out = []
for _ in range(m):
    parts = input().split()
    if parts[0] == "add":
        kind, name = parts[1], parts[2]
        price, qty, extra = int(parts[3]), int(parts[4]), int(parts[5])
        if kind == "food":
            items[name] = Food(name, price, qty, extra)
        else:
            items[name] = Tool(name, price, qty, extra)
    elif parts[0] == "sell":
        name, amount = parts[1], int(parts[2])
        if name in items:
            items[name].qty = max(0, items[name].qty - amount)
    else:
        rows = sorted(items.values(), key=lambda it: (-it.value(), it.name))
        for it in rows:
            out.append(f"{it.name} {it.value():.1f}")

print("\n".join(out))
