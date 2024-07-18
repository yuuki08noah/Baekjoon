arr1 = []
arr2 = []
n, m = map(int, input().split())
for i in range(n):
    temp = list(map(int, input().split()))
    arr1.append(temp)

n, m = map(int, input().split())
for i in range(n):
    temp = list(map(int, input().split()))
    arr2.append(temp)
arr3 = []

for i in range(len(arr1)):

    temp = []
    for j in range(m):

        sum=0
        for k in range(len(arr1[i])):
            sum+=arr1[i][k]*arr2[k][j]

        temp.append(sum)

    arr3.append(temp)

for i in range(len(arr3)):
    for j in range(len(arr3[i])):
        print(arr3[i][j],end=" ")

    print()