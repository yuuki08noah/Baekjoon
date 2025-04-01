import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split())) + [0, 0]
cnt = 0
i = 0

def b1(i):
    global cnt
    min_val = min(arr[i], arr[i + 1], arr[i + 2])
    cnt += 7 * min_val
    arr[i] -= min_val
    arr[i + 1] -= min_val
    arr[i + 2] -= min_val

def b2(i):
    global cnt
    min_val = min(arr[i], arr[i + 1])
    cnt += 5 * min_val
    arr[i] -= min_val
    arr[i + 1] -= min_val

def b3(i):
    global cnt
    cnt += 3 * arr[i]
    arr[i] = 0

while i < n:
    if arr[i+1] > arr[i+2]:
        min_val = min(arr[i], arr[i+1] - arr[i+2])
        cnt += 5 * min_val
        arr[i] -= min_val
        arr[i+1] -= min_val
        b1(i)
        b3(i)
    else:
        b1(i)
        b2(i)
        b3(i)
    i += 1

print(cnt)