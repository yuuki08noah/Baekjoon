import sys
from collections import deque

sys = sys.stdin.readline
n, m = map(int, input().split())
in_degree = [0] * n
table = {}
for _ in range(m):
    x, y = map(int, input().split())
    in_degree[y-1] += 1
    if x not in table:
        table[x] = [y]
    else:
        table[x].append(y)

queue = deque([i+1 for i in range(n) if in_degree[i] == 0])
while queue:
    x = queue.popleft()
    print(x, end=' ')
    if x in table:
        for i in table[x]:
            in_degree[i-1] -= 1
            if in_degree[i-1] == 0:
                queue.append(i)
