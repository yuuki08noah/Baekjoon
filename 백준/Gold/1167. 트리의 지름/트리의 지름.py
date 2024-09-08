import sys
from collections import deque
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
table = {i:[] for i in range(1, n+1)}

visited = [False] * (n+1)

for i in range(n):
    nodes = list(map(int, input().split()))
    start = nodes[0]
    idx = 1
    while nodes[idx] != -1:  # -1이 나올 때까지 반복
        to = nodes[idx]
        dist = nodes[idx + 1]
        table[start].append((to, dist))
        table[to].append((start, dist))  # 양방향 연결
        idx += 2
def dfs(start, s):
    visited[start] = True
    far = start
    max_dist = s
    if start in table:
        for node, d in table[start]:
            if not visited[node]:
                new_far, new_max_dist = dfs(node, s + d)
                if new_max_dist > max_dist:
                    max_dist = new_max_dist
                    far = new_far
    return far, max_dist

far, _ = dfs(1, 0)

visited = [False] * (n+1)
_, max_d = dfs(far, 0)
print(max_d)