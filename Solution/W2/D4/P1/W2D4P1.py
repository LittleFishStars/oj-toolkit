n = int(input())

for d in range(2, n):
    if n % d == 0:
        print(0)
        break
else:
    print(1)
