import sys

input = sys.stdin.readline().strip
n = int(input())
arr = [i for i in range(1, n+1)]
while len(arr) > 1:
    print(arr[0], end=' ')
    del arr[0]
    arr.append(arr[0])
    del arr[0]
print(arr[0])