import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [0]
max_num = arr[0]
min_num = arr[0]

for i in range(n):
    min_num = min(min_num, arr[i])
    res.append(max(res[-1], arr[i]-min_num))
print(*res[1:])