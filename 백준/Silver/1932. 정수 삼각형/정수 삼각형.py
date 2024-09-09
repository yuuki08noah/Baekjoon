import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.insert(0, list(map(int, input().split())))
for i in range(n-1):
    for j in range(len(graph[i+1])):
        graph[i+1][j] += max(graph[i][j], graph[i][j+1])

print(graph[-1][-1])