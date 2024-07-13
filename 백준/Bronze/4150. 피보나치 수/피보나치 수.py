
n = int(input())
arr = [1, 1]

if n==0:
    print(1)
elif n<=1:
    print(1)
else:
    for i in range(n+1):
        arr.append(arr[i+1]+arr[i+0])
    
    print(arr[n-1])