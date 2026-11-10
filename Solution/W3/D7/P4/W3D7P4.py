class Book:
    def __init__(self, title, price, stock):
        self.title = title
        self.price = price
        self.stock = stock

    def value(self):
        return self.price * self.stock

    def __str__(self):
        return self.title

    def __lt__(self, other):
        return self.value() < other.value()

    def __add__(self, other):
        return Combo(self, other)


class Ebook(Book):
    def __init__(self, title, price, stock, mb):
        super().__init__(title, price, stock)
        self.mb = mb

    def __str__(self):
        return f"{self.title}[电子]"


class Paper(Book):
    def __init__(self, title, price, stock, kg):
        super().__init__(title, price, stock)
        self.kg = kg

    def __str__(self):
        return f"{self.title}[纸质]"


class Combo(Book):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def value(self):
        return self.left.value() + self.right.value()

    def __str__(self):
        return "组合"


m = int(input())
books = {}
out = []
for _ in range(m):
    parts = input().split()
    if parts[0] == "add":
        kind, title = parts[1], parts[2]
        price, stock, extra = int(parts[3]), int(parts[4]), int(parts[5])
        if kind == "ebook":
            books[title] = Ebook(title, price, stock, extra)
        else:
            books[title] = Paper(title, price, stock, extra)
    elif parts[0] == "sell":
        title, amount = parts[1], int(parts[2])
        if title in books:
            books[title].stock = max(0, books[title].stock - amount)
    elif parts[0] == "list":
        rows = sorted(books.values(), key=lambda b: (-b.value(), str(b)))
        for b in rows:
            out.append(f"{b} {b.value():.1f}")
    else:
        total = 0
        for b in books.values():
            total += b.value()
        out.append(f"{total:.1f}")

print("\n".join(out))
