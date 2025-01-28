import sys

input = sys.stdin.readline
s = input().strip()
arr = [(0, 0)]
for i in range(len(s)-1):
    la, lb = arr[-1][0], arr[-1][1]
    if s[i] == s[i+1] == '(':
        la += 1
    elif s[i] == s[i+1] == ')':
        lb += 1
    arr.append((la, lb))

# print(arr)
res = 0
a, b = arr[0]
for i in range(len(arr)):
    if arr[i][0] > a:
        res += arr[-1][1] - arr[i][1]
        a = arr[i][0]
print(res)