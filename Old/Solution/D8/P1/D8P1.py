N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u - 1][v - 1] = 1
    adj[v - 1][u - 1] = 1
for row in adj:
    print(*row)
