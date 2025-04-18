from collections import deque

init = input().replace(' ', '')
def bfs(init):
    final = "12345678x"
    queue = deque([init])
    visited = {init: 0}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current = queue.popleft()
        if current == final:
            return visited[current]
        idx = current.index('x')
        x, y = idx // 3, idx % 3
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                lst = list(current)
                new_idx = nx * 3 + ny
                lst[idx], lst[new_idx] = lst[new_idx], lst[idx]
                new_state = ''.join(lst)
                if new_state not in visited:
                    visited[new_state] = visited[current] + 1
                    queue.append(new_state)
    return -1

print(bfs(init))
    