
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
table = {i:[] for i in range(1, n+1)}
matched = {}

for k in range(m):
    a, b = map(int, input().split())
    table[a].append(b)

def dfs(x):
    for i in table[x]:
        if visited[i]:
            continue
        visited[i] = True
        if i not in matched or dfs(matched[i]):
            matched[i] = x
            return True
    return False

cnt = 0
for i in range(1, n+1):
    visited = [False] * 500000
    if dfs(i):
        cnt += 1
print(cnt)