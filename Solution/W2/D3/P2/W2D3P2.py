n = int(input())

answer = n
for d in range(2, n + 1):
    if n % d == 0:
        answer = d
        break
print(answer)
