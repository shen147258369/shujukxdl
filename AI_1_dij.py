n, m = map(int, input().split())
INF = float('inf')
adj = [[INF] * (n + 1) for _ in range(n + 1)]
dist = [INF] * (n + 1)
visited = [False] * (n + 1)

def dijkstra():
    dist[1] = 0
    for i in range(n):
        t = -1
        for j in range(1, n + 1):
            if not visited[j] and (t == -1 or dist[t] > dist[j]):
                t = j
        visited[t] = True
        for j in range(1, n + 1):
            dist[j] = min(dist[j], dist[t] + adj[t][j])
    if dist[n] >= INF:
        return -1
    else:
        return dist[n]

for _ in range(m):
    x, y, z = map(int, input().split())
    adj[x][y] = min(adj[x][y], z)

print(dijkstra())