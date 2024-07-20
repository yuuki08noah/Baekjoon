arr1 = []
arr2 = []
arr3 = []
n = int(input())
for i in range(n):
    temp = list(map(int, input().split()))
    arr1.append(temp)
for j in range(n):
    temp = list(map(int, input().split()))
    arr2.append(temp)

for i in range(len(arr1)):
    temp = []
    for j in range(len(arr1)):

        sum=0
        for k in range(len(arr1[i])):
            sum+=arr1[i][k]*arr2[k][j]

        temp.append(sum)

    arr3.append(temp)

sum = 0
for i in range(len(arr3)):
    for j in range(len(arr3[i])):
        sum+=1 if arr3[i][j]>0 else 0

print(sum)