import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().split()))[1:] for _ in range(n)]

def dfs(i):
    if visited[i]:
        return False
    visited[i] = True
    for j in graph[i]:
        if work[j] == -1:
            work[j] = i
            return True
    for j in graph[i]:
        if dfs(work[j]):
            work[j] = i
            return True
    return False

work = [-1 for _ in range(m+1)]
for i in range(n):
    visited = [False] * n
    dfs(i)
success = 0
for i in range(n):
    if success >= k:
        break
    visited = [False] * n
    success += int(dfs(i))
print(m-work.count(-1)+1)

