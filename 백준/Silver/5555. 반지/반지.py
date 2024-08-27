import sys

input = sys.stdin.readline
s = input().strip()
n = int(input())
cnt = 0
for i in range(n):
    m = input().strip()
    m = m*2
    if s in m:
        cnt += 1
print(cnt)