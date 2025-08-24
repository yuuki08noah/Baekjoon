import sys

input = sys.stdin.readline

n = int(input())
graph = [[j for j in range(n) if j != i] for i in range(n)]
cost = [list(map(int, input().split())) for _ in range(n)]
def dfs(i):
    if visited[i]:
        return False
    visited[i] = True
    # if work.count(-1) == 1: return False
    for j in graph[i]:
        if cost[i][0] < cost[j][0] or \
            cost[i][1] < cost[j][1] or \
            cost[i][2] < cost[j][2]:
            continue
        if cost[i][0] == cost[j][0] and cost[i][1] == cost[j][1] and cost[i][2] == cost[j][2]:
            if i >= j: continue
        if work[j] == -1:
            work[j] = i
            return True
    for j in graph[i]:
        if cost[i][0] < cost[j][0] or \
            cost[i][1] < cost[j][1] or \
            cost[i][2] < cost[j][2]:
            continue
        if cost[i][0] == cost[j][0] and cost[i][1] == cost[j][1] and cost[i][2] == cost[j][2]:
            if i >= j: continue
        if dfs(work[j]):
            work[j] = i
            return True
    return False

work = [-1 for _ in range(n)]
for i in range(n):
    visited = [False] * n
    dfs(i)
    visited = [False] * n
    dfs(i)
print(work.count(-1))

