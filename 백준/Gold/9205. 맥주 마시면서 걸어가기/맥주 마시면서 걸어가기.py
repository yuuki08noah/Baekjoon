import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    sk = tuple(map(int, input().split()))
    conve = []
    for i in range(n):
        conve.append(tuple(map(int, input().split())))
    visited = {}
    fes = tuple(map(int, input().split()))

    queue = deque([sk])
    beer = 20
    flag = True

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited[(x, y)] = True
        if abs(fes[0] - x) + abs(fes[1] - y) <= beer * 50:
            print('happy')
            flag = False
            break
        for i in range(len(conve)):
            if abs(conve[i][0] - x) + abs(conve[i][1] - y) <= 50*beer and conve[i] not in visited:
                queue.append(conve[i])
                beer = 20
    if flag:
        print('sad')