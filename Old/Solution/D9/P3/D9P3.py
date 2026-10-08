N = int(input())
depth = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    depth[v] = depth[u] + 1
for i in range(1, N + 1):
    print(depth[i])
