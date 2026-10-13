target = int(input())

count = 0
n = 2
while count < target:
    for d in range(2, n):
        if n % d == 0:
            break
    else:
        count += 1
        if count == target:
            print(n)
    n += 1
