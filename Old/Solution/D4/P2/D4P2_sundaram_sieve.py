n = int(input())
if n < 2:
    print()
    exit()

primes = [2]
if n == 2:
    print(2)
    exit()

k = (n - 1) // 2
marked = [False] * (k + 1)

for i in range(1, k + 1):
    for j in range(i, k + 1):
        idx = i + j + 2 * i * j
        if idx > k:
            break
        marked[idx] = True

for i in range(1, k + 1):
    if not marked[i]:
        primes.append(2 * i + 1)

print(' '.join(map(str, primes)))
