import sys

input = sys.stdin.readline
n = int(input())
arr = [input().strip() for _ in range(n)]

con = 3
for k in range(n-1):
    # print(con)
    if arr[k] <= arr[k+1] and (con == 3 or con == 1):
        con = 1
    elif arr[k] >= arr[k+1] and (con == 3 or con == 2):
        con = 2
    else:
        con = 4
        break
print("DECREASING" if con == 2 else "INCREASING" if con == 1 else "NEITHER")
