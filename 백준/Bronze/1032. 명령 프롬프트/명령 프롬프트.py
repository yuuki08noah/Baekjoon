arr = []
for _ in range(int(input())):
    arr.append(input().strip())
base = list(arr[0])
for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] != base[j]:
            base[j] = '?'
print(''.join(base))
    