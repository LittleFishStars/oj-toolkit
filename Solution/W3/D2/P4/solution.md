Python
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Classroom:
    def __init__(self, students):
        self.students = students

    def best(self):
        best = self.students[0]
        for s in self.students:
            if s.score > best.score:
                best = s
        return best.name

    def average(self):
        total = 0
        for s in self.students:
            total += s.score
        return total / len(self.students)

    def above(self):
        average = self.average()
        count = 0
        for s in self.students:
            if s.score > average:
                count += 1
        return count


n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append(Student(name, int(score)))

c = Classroom(students)
print(c.best())
print(f"{c.average():.2f}")
print(c.above())
```
