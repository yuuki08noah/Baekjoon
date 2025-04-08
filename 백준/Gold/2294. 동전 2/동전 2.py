import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])
arr = [0]

for i in range(1, k+1):
    m = 10**9
    for c in coins:
        if c <= i:
            m = min(m, arr[i-c] + 1)
    arr.append(m)

print(arr[k] if arr[k] != 10**9 else -1)