import sys

input = sys.stdin.readline
n = int(input())
temp = n
cnt = 0
while True:
    temp = (temp % 10) * 10 + (temp % 10 + (temp // 10) % 10) % 10
    cnt += 1
    if temp == n:
        break
print(cnt)