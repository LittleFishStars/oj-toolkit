n = int(input())
limit = max(1000000, n * 13)
is_prime = bytearray(b'\x01') * (limit + 1)
is_prime[0] = is_prime[1] = 0
for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        is_prime[i * i:limit + 1:i] = b'\x00' * ((limit - i * i) // i + 1)
cnt = 0
for i in range(2, limit + 1):
    if is_prime[i]:
        cnt += 1
        if cnt == n:
            print(i)
            break
