def dfs():
    init = input().replace(' ', '')
    final = "12345678x"
    visited = set()
    stack = [(init, 0)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while stack:
        state, _ = stack.pop()
        if state == final:
            return 1
        if state in visited:
            continue
        visited.add(state)
        idx = state.index('x')
        x, y = idx // 3, idx % 3
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                lst = list(state)
                new_idx = nx * 3 + ny
                lst[idx], lst[new_idx] = lst[new_idx], lst[idx]
                new_state = ''.join(lst)
                if new_state not in visited:
                    stack.append((new_state, 0))
    return 0
print(dfs())