import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def dfs(idx, s, selected):
    global cnt
    if idx == n:
        if s == m and selected: cnt += 1
        return
    dfs(idx+1, s+arr[idx], selected+1)
    dfs(idx+1, s, selected)
dfs(0, 0, 0)
print(cnt)