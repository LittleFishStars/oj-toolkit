n = int(input())
entries = []
for i in range(n):
    name, age = input().split()
    entries.append((int(age), i, name))
entries.sort()
for age, _, name in entries:
    print(name, age)
