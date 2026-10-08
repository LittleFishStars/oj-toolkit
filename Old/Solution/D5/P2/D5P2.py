n = int(input())
entries = []
for i in range(n):
    name, age = input().split()
    entries.append((name, int(age), i))
entries.sort(key=lambda x: (x[0], x[1], x[2]))
for name, age, _ in entries:
    print(name, age)
