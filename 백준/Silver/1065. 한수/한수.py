import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cnt = 0

def check(n):
    global cnt
    if n <= 9:
        cnt += 1
        return
    else:
        k = int(str(n)[0]) - int(str(n)[1])
        for i in range(1, len(str(n))-1):
            if int(str(n)[i]) - int(str(n)[i+1]) != k:
                return
        cnt += 1

for i in range(1, n+1):
    check(i)
print(cnt)