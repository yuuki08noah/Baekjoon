import sys

input = sys.stdin.readline
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
matrix.sort(key=lambda x: x[2], reverse=True)
res = []
con = []
for row in matrix:
    if len(res) == 3:
        break
    if con.count(row[0]) >= 2:
        continue
    else:
        res.append(row)
        con.append(row[0])
for i in res:
    print(i[0], i[1])

