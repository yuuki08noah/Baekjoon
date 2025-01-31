import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    input()
    n, k = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    queries = [tuple(map(lambda x: int(x)+1, input().split())) for _ in range(k)]
    for i in range(2, n+1):
        arr[i] += arr[i-1]
    for x, y in queries:
        print(arr[y]-arr[x-1])
    print()