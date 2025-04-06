import sys
input = sys.stdin.readline

n = int(input())
arr = [0, 1, 1, 2, 2, 1, 2, 1]
for i in range(8, n+1):
    arr.append(min(arr[i-1], arr[i-2], arr[i-5], arr[i-7])+1)
print(arr[n])