import sys

input = sys.stdin.readline
n, m = map(int, input().split())
s = []
def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n+1):
        if i in s: continue  # Skip duplicates
        s.append(i)
        dfs()
        s.pop()
dfs()