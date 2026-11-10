class Animal:
    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "wang"


class Cat(Animal):
    def speak(self):
        return "miao"


word = input()
if word == "dog":
    a = Dog()
else:
    a = Cat()
print(a.speak())
