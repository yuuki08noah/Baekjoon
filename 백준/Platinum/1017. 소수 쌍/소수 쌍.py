import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

graph = {i:[j for j in arr if i != j and is_prime(i+j)] for i in arr}
res = set()

def dfs(i):
    if visited[i]:
        return False
    visited[i] = True
    # if work.count(-1) == 1: return False
    for j in graph[i]:
        if work[j] == -1:
            work[j] = i
            return True
    for j in graph[i]:
        if work[j] != arr[0] and dfs(work[j]):
            work[j] = i
            return True
    return False

for i in graph[arr[0]]:
    work = {_: -1 for _ in arr}
    work[i] = arr[0]
    matched = 1
    for j in arr:
        if j == arr[0]: continue
        if j % 2 != arr[0] % 2: continue
        visited = [False] * 1001
        matched += dfs(j)

    if matched == n // 2:
        res.add(i)
print(*([i for i in sorted(res)] if res else [-1]))

