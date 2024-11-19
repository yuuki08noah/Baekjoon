import sys

input = sys.stdin.readline

s = input().strip()
arr = [0] * 10
f = 0
for k in s:
    if (k == '9' or k == '6') and f == 0:
        f = 1
        arr[9] += 1
    elif (k == '9' or k == '6') and f == 1:
        f = 0
        arr[6] += 1
    else:
        arr[int(k)] += 1
print(max(arr))