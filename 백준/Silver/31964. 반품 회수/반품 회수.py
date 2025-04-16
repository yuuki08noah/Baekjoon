import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
distance = [0] + list(map(int, input().split()))
visited = [False] * n
time = list(map(int, input().split()))

t = 0
for i in range(n):
    if distance[i+1] >= time[i]:
        visited[i] = True
t = distance[-1]
# print(t)
for i in range(n-1, -1, -1):
    # print(t)
    while not visited[i] and time[i] > t:
        t += 1
    t += distance[i+1] - distance[i]
    visited[i] = True

print(t)
