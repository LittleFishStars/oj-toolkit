class Seq:
    def __init__(self, a, d, n):
        self.a = a
        self.d = d
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        return self.a + self.d * i

    def __iter__(self):
        for i in range(self.n):
            yield self[i]

    def __str__(self):
        return " ".join(str(x) for x in self)


a, d, n = map(int, input().split())
seq = Seq(a, d, n)
print(seq)

q = int(input())
for _ in range(q):
    i = int(input())
    print(seq[i])
