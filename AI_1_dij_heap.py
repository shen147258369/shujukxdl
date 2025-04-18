import heapq

n, m = map(int, input().split())
INF = float('inf')
adj = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    adj[x].append((y, z))

def dijkstra():
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        current_dist, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    if dist[n] >= INF:
        return -1
    else:
        return dist[n]
print(dijkstra())