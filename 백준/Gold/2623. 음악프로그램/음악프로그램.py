import sys
from collections import deque

sys = sys.stdin.readline
n, m = map(int, input().split())
in_degree = [0] * n
table = {i: [] for i in range(1, n+1)}
for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1):
        table[arr[i]].append(arr[i+1])
        in_degree[arr[i+1]-1] += 1

# print(table)
queue = deque([i+1 for i in range(n) if in_degree[i] == 0])
res = []
while queue:
    x = queue.popleft()
    res.append(x)
    if x in table:
        for i in table[x]:
            in_degree[i-1] -= 1
            if in_degree[i-1] == 0:
                queue.append(i)
if len(res) != n:
    print(0)
else:
    print(*res, sep='\n')