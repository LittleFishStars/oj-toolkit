class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def level(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "E"

    def card(self):
        return f"{self.name}:{self.score} 等级{self.level()}"


name, score = input().split()
s = Student(name, int(score))
print(s.card())
