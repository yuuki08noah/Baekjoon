import sys


input = sys.stdin.readline
n = int(input())
cnt = 0

while n % 5 != 0:
    n -= 3
    cnt += 1
    if n < 0:
        print(-1)
        exit()

cnt += n//5
print(cnt)