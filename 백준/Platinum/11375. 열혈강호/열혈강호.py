import sys

input = sys.stdin.readline
n, m = map(int, input().split())
table = {i:[] for i in range(1, n+1)}
matched = {}

for k in range(1, n+1):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)):
        table[k].append(arr[i])

def dfs(x):
    for i in table[x]:
        if visited[i-1]:
            continue
        visited[i-1] = True
        if i not in matched or dfs(matched[i]):
            matched[i] = x
            return True
    return False

cnt = 0
for i in range(1, n+1):
    visited = [False] * m
    if dfs(i):
        cnt += 1
print(cnt)