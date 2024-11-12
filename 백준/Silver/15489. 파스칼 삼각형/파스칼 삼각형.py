import sys

input = sys.stdin.readline
r, c, w = map(int, input().split())
pascal = [[0] * 30 for _ in range(30)]
for i in range(0, 30):
    for j in range(0, i+1):
        if i == j or j == 0:
            pascal[i][j] = 1
        elif j == 1:
            pascal[i][j] = i
        else:
            pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
# print(*pascal, sep='\n')
res = 0
for i in range(r - 1, r + w - 1):
    for j in range(i - r + 2):
        # print(i, j, pascal[i][j + c - 1])
        res += pascal[i][j + c - 1]
print(res)