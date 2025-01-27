import sys
input = sys.stdin.readline
n = int(input())
grades = [0, 0, 0, 0, 0, 0]
la, lb = map(int, input().split())
last = [0, 0, 0, 0, 0, 0]
last[la] = 1
last[lb] = 1
for i in range(1, n):
    k = list(map(int, input().split()))
    last[k[0]] += 1
    last[k[1]] += 1 if k[1] != k[0] else 0

    if la not in k:
        grades[la] = max(last[la], grades[la])
        last[la] = 0
    if lb not in k:
        grades[lb] = max(last[lb], grades[lb])
        last[lb] = 0
    la, lb = k[0], k[1]

grades[la] = max(grades[la], last[la])
grades[lb] = max(grades[lb], last[lb])
# print(grades)
print(max(grades), grades.index(max(grades)))
