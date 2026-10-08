N = int(input())
children = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    children[u].append(v)
for i in range(1, N + 1):
    children[i].sort()
    if children[i]:
        print(f"{i}:", *children[i])
    else:
        print(f"{i}:")
