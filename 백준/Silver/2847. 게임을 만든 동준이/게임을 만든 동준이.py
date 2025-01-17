n = int(input())
li = [0] * n
cnt = 0

for x in range(n):
    li[x] = int(input())

for x in range(n - 1, 0, -1):
    while li[x] <= li[x - 1]:
        li[x - 1] -= 1
        cnt += 1

print(cnt)

