Python
```python
class Analyzer:
    def __init__(self, names, scores):
        self.names = names
        self.scores = scores

    def count(self):
        return len(self.scores)

    def average(self):
        return sum(self.scores) / len(self.scores)

    def best(self):
        best = 0
        for k in range(len(self.scores)):
            if self.scores[k] > self.scores[best]:
                best = k
        return self.names[best]

    def pass_rate(self):
        passed = 0
        for s in self.scores:
            if s >= 60:
                passed += 1
        return passed / len(self.scores) * 100


n = int(input())
names, scores = [], []
for _ in range(n):
    name, score = input().split()
    names.append(name)
    scores.append(int(score))

a = Analyzer(names, scores)
print(f"{a.count()} {a.average():.2f}")
print(a.best())
print(f"{a.pass_rate():.1f}%")
```
