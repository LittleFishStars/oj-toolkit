n = int(input())

names = []
scores = []
for k in range(n):
    name, score = input().split()
    names.append(name)
    scores.append(int(score))

best = 0
for k in range(n):
    if scores[k] > scores[best]:
        best = k

total = 0
for s in scores:
    total += s
average = total / n

above = 0
for s in scores:
    if s > average:
        above += 1

print(names[best])
print(f"{average:.2f}")
print(above)
