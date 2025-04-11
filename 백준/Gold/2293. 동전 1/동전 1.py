import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])
arr = [0] * (k+1)
arr[0] = 1

for c in coins:
    for i in range(c, k + 1):
        arr[i] += arr[i-c]

print(arr[k])