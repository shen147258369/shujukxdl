import heapq

init = input().replace(' ', '')
subs = init.replace('x', '')

def manhadun(state):
    res = 0
    for i in range(len(state)):
        if state[i] != 'x':
            t = ord(state[i])
            res += abs(i // 3 - t // 3) + abs(i % 3 - t % 3) # 曼哈顿距离的和
    return res

def a_star(init):
    final, fx = "12345678x", "urdl"
    dist, prev = {}, {}
    heap = []
    dist[init] = 0
    heapq.heappush(heap, (manhadun(init), init))
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    while heap:
        t, state = heapq.heappop(heap)
        if init == final:
            break
        x, y = 0, 0
        for i in range(9):
            if state[i] == 'x':
                x, y = i // 3, i % 3
                break
        source = state
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if a < 0 or a >= 3 or b < 0 or b >= 3:
                continue
            now = source
            z, p = now[x * 3 + y], now[a * 3 + b]
            now = now.replace(z, 'q')
            now = now.replace(p, z)
            now = now.replace('q', p)
            if (now not in dist or dist[now] > dist[source] + 1):
                dist[now] = dist[source] + 1
                prev[now] = (fx[i], source)
                heapq.heappush(heap, (dist[now] + manhadun(now), now))
    res = ""
    while final != init:
        xx, yy = prev[final]
        res += xx
        final = yy
    return res[::-1]

count = 0
for i in range(8):
    for j in range(i, 8):
        if subs[i] > subs[j]:
            count += 1
if count % 2 != 0:
    print("unsolvable")
else:
    print(a_star(init))
    