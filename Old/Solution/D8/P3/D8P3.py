N, M = map(int, input().split())
mat = [[0] * M for _ in range(N)]
for j in range(M):
    u, v = map(int, input().split())
    mat[u - 1][j] = 1
    mat[v - 1][j] = 1
for row in mat:
    print(*row)
