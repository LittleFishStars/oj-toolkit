N = int(input())
parent = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    parent[v] = u
for i in range(1, N + 1):
    print(parent[i])
