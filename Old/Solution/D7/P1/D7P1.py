L, M = map(int, input().split())
trees = [1] * (L + 1)
for _ in range(M):
    u, v = map(int, input().split())
    for j in range(u, v + 1):
        trees[j] = 0
print(sum(trees))
