import sys

input = sys.stdin.readline
t = int(input())
arr = []
for i in range(666, 3000000):
    if '666' in str(i):
        arr.append(i)
print(arr[t-1])