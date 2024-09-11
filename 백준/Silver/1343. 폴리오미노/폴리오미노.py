import sys
from collections import deque
import heapq

input = sys.stdin.readline
str = input().strip().split('.')
res = ''
i = 1
for line in str:
    if len(line) % 2 == 0:
        res += 'AAAA'*(len(line)//4)
        res += 'BB'*((len(line)%4)//2)
    else:
        print(-1)
        exit()
    if i == len(str):
        break
    res += '.'
    i += 1
print(res)

