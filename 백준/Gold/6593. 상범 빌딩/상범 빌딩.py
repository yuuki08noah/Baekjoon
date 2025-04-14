import sys
from collections import deque

input = sys.stdin.readline

while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break
    building = []
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    s = ()
    dx = [0, 0, 1, -1, 0, 0]
    dy = [0, 0, 0, 0, 1, -1]
    dz = [-1, 1, 0, 0, 0, 0]
    for i in range(l):
        floor = []
        for j in range(r):
            arr = list(input().strip())
            if 'S' in arr:
                s = (i, j, arr.index('S'), 0)
            floor.append(arr)
        input()
        building.append(floor)

    queue = deque([s])
    flag = True
    while queue:
        x, y, z, depth = queue.popleft()
        for nx, ny, nz in zip(dx, dy, dz):
            new_x, new_y, new_z = x + nx, y + ny, z + nz
            if 0 <= new_x < l and 0 <= new_y < r and 0 <= new_z < c and not visited[new_x][new_y][new_z] and building[new_x][new_y][new_z] != '#':
                visited[new_x][new_y][new_z] = True
                if building[new_x][new_y][new_z] == 'E':
                    print(f"Escaped in {depth+1} minute(s).")
                    flag = False
                    break
                queue.append((new_x, new_y, new_z, depth + 1))
    if flag: print("Trapped!")
