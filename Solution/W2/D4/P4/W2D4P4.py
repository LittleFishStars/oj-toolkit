n = int(input())

parts = []
d = 2
while n > 1:
    while n % d == 0:
        parts.append(str(d))
        n //= d
    d += 1
print("*".join(parts))
