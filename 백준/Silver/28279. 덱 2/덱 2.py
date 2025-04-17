import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
d = deque()
for i in range(n):
    inp = input().split()
    a = int(inp[0])
    b = 0
    if len(inp) > 1:
        b = int(inp[1])
    if a == 1:
        d.appendleft(b)
    elif a == 2:
        d.append(b)
    elif a == 3:
        if len(d) > 0: print(d.popleft())
        else: print(-1)
    elif a == 4:
        if len(d) > 0: print(d.pop())
        else: print(-1)
    elif a == 5:
        print(len(d))
    elif a == 6:
        print(int(len(d) == 0))
    elif a == 7:
        if len(d) > 0: print(d[0])
        else: print(-1)
    else:
        if len(d) > 0: print(d[len(d)-1])
        else: print(-1)
