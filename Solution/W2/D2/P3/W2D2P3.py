n = int(input())

a, b = 1, 1
count = 0
while count < n:
    print(a)
    nxt = a + b
    a = b
    b = nxt
    count += 1
