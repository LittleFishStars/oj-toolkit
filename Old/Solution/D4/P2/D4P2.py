n = int(input())
if n < 2:
    print()
    exit()
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        is_prime[i * i:n + 1:i] = [False] * ((n - i * i) // i + 1)
print(' '.join(str(i) for i in range(2, n + 1) if is_prime[i]))
