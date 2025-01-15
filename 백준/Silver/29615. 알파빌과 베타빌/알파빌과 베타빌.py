import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
friend = list(map(int, input().split()))
arr = list(map(lambda x: int(x in friend), arr))
cnt = 0
for i in range(n):
    if arr[i] == 0:
        for j in range(n - 1, i, -1):
            if arr[j] == 1:
                cnt += 1
                arr[i], arr[j] = arr[j], arr[i]
                break
print(cnt)