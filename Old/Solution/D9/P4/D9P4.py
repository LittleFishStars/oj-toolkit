N = int(input())
has_child = [False] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    has_child[u] = True
print(sum(1 for i in range(1, N + 1) if not has_child[i]))
