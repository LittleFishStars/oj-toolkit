a, b = map(int, input().split())

count = 0
for n in range(a, b + 1):
    for d in range(2, n):
        if n % d == 0:
            break
    else:
        count += 1
print(count)
