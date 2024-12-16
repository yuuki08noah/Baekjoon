n, m = map(int, input().split())
arr = [1, 1]
for i in range(2, n+1): 
    arr.append(i * arr[-1])
print(arr[n]//(arr[m]*arr[n-m]))