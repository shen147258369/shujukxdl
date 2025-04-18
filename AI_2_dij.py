import heapq

init = input().replace(' ', '')
subs = init.replace('x', '')
final = "12345678x"

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, init))
    visited = {init: 0}
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while heap:
        dist, current = heapq.heappop(heap)
        if current == final:
            return dist
        if dist > visited.get(current, float('inf')):
            continue
        idx = current.index('x')
        x, y = idx // 3, idx % 3
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                lst = list(current)
                new_idx = nx * 3 + ny
                lst[idx], lst[new_idx] = lst[new_idx], lst[idx]
                new_state = ''.join(lst)
                new_dist = dist + 1
                if new_state not in visited or new_dist < visited[new_state]:
                    visited[new_state] = new_dist
                    heapq.heappush(heap, (new_dist, new_state))
    return -1

count = 0
for i in range(8):
    for j in range(i+1, 8):
        if subs[i] > subs[j]:
            count += 1
if count % 2 != 0:
    print(-1)
else:
    res = dijkstra()
    print(res if res != -1 else -1)