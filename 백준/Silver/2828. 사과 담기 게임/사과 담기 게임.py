import sys

input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())
index = 0
cnt = 0
for i in range(k):
    arr = [0] * n
    l = int(input())
    arr[l-1] = 1
    if 1 in arr[index:index+m]:
        continue
    else:
        if l > index+m:
            while True:
                index += 1
                cnt += 1
                if 1 in arr[index:index+m]:
                    break
        elif l < index+m:
            while True:
                index -= 1
                cnt += 1
                if 1 in arr[index:index+m]:
                    break
print(cnt)