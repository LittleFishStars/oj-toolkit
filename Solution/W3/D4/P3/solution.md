Python
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        return self.name < other.name

    def __str__(self):
        return f"{self.name} {self.score}"


n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append(Student(name, int(score)))

for s in sorted(students):
    print(s)
```
