N = int(input())
children = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    children[u].append(v)

size = [1] * (N + 1)
order = []

def dfs(u):
    order.append(u)
    for v in children[u]:
        dfs(v)

dfs(1)
for u in reversed(order):
    for v in children[u]:
        size[u] += size[v]

for i in range(1, N + 1):
    print(size[i])
