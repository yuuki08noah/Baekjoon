from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    sorted_arr = deque(sorted(arr, reverse=True))
    for i in range(n):
        arr[i] = (arr[i], i)
    arr = deque(arr)
    cnt = 0
    while arr:
        k, i = arr.popleft()
        l = sorted_arr.popleft()
        if k != l:
            arr.append((k, i))
            sorted_arr.appendleft(l)
        if k == l:
            cnt += 1
        if k == l and i == m:
            print(cnt)
            break