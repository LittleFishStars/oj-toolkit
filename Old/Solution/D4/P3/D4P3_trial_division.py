def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


p = int(input())
idx = 0
for i in range(2, p + 1):
    if is_prime(i):
        idx += 1
        if i == p:
            print(idx)
            break
