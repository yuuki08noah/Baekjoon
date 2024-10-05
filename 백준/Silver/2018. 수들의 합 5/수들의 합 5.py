import sys

input = sys.stdin.readline
n = int(input())

cnt = 0
for i in range(1, n + 1):
    base = (i * (i + 1)) // 2
    if base > n:
        break
    if (n - base) % i == 0:
        cnt += 1

print(cnt)