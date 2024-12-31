import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
k = 1
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print("Case #{}:".format(k), end=' ')
    k += 1
    for i in arr:
        # print(i, (i // 3) * 4)
        if i == 0: continue
        if (i // 3) * 4 in arr:
            print(i, end=' ')
            arr[arr.index((i // 3) * 4)] = 0
            arr[arr.index(i)] = 0
    print()