import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = []
score = [0] * n
for i in range(n):
    li.append([list(map(int, input().split())), 0])
    li[i][1] = max(li[i][0])
for i in range(m):
    k = max(map(lambda x: x[1], li))
    for j in range(n):
        if li[j][1] == k:
            score[j] += 1
        del li[j][0][li[j][0].index(max(li[j][0]))]
        li[j][1] = max(li[j][0] if len(li[j][0]) > 0 else (0, 0))

for i in range(n):
    if score[i] == max(score): print(i+1, end=" ")