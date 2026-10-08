p = int(input())
is_prime = [True] * (p + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(p ** 0.5) + 1):
    if is_prime[i]:
        is_prime[i * i:p + 1:i] = [False] * ((p - i * i) // i + 1)
idx = 0
for i in range(2, p + 1):
    if is_prime[i]:
        idx += 1
        if i == p:
            print(idx)
            break
