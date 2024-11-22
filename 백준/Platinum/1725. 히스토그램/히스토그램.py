import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.insert(0, n)
stack = []
m = 0

for i in range(1, len(arr)):
    if not stack or arr[i] >= stack[-1][1]:
        stack.append((i, arr[i]))
    else:
        while stack and stack[-1][1] > arr[i]:
            k = stack.pop()
            m = max(m, k[1] * (i - stack[-1][0] - 1 if stack else i-1))
        stack.append((i, arr[i]))
# print(m)
while stack:
    k = stack.pop()
    if len(stack) == 0:
        width = len(arr) - 1
    else:
        width = len(arr) - stack[-1][0] - 1
    m = max(m, k[1] * width)
print(m)