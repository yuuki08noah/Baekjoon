import sys

input = sys.stdin.readline
n, m = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    while i // 10 != 0:
        if i % 10 == m: cnt += 1
        i //= 10
    if i == m: cnt += 1
print(cnt)