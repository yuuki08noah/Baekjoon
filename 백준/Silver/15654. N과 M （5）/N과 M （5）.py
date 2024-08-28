import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
s = []
def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n+1):
        if arr[-i] in s:
            continue
        s.append(arr[-i])
        dfs()
        s.pop()
dfs()