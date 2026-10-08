N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u - 1].append(v)
    adj[v - 1].append(u)
for i in range(N):
    adj[i].sort()
    if adj[i]:
        print(f"{i + 1}:", *adj[i])
    else:
        print(f"{i + 1}:")
