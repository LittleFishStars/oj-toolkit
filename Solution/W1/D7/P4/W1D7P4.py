age, student, member = map(int, input().split())
if age < 6 or age >= 60:
    print(0)
elif student == 1:
    print(5)
elif member == 1:
    print(9)
else:
    print(10)
