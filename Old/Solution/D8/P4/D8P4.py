N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    edges.append((u, v))
edges.sort()
for u, v in edges:
    print(u, v)
