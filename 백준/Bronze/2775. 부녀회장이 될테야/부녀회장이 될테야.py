import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    arr = [[i for i in range(n + 1)]]
    for i in range(k):
        temp = [0]
        for j in range(1, n + 1):
            temp.append(temp[-1] + arr[-1][j])
        arr.append(temp)
    print(arr[k][n])
