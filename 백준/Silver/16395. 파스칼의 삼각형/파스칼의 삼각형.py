import math

n, m = map(int, input().split())

arr = [1]
for i in range(2, 102):
    arr.append(i * arr[i-2])

n-=1
m-=1
print((arr[n-1] // (arr[m-1] * arr[n-m-1])) if (arr[n-1] // (arr[m-1] * arr[n-m-1]))!=0 else 1)

