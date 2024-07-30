import sys
import math

input = sys.stdin.readline
n, m = map(int, input().split())
inputs = list(map(int, input().split()))
arr = [inputs[0]]
cnt = 0
remainder = [inputs[0]%m]
for i in range(1, len(inputs)):
    arr.append((inputs[i]+arr[-1]))
    remainder.append(arr[-1]%m)

temp = set(remainder)
for i in temp:
    cnt += remainder.count(i)*(remainder.count(i)-1)//2
print(cnt+remainder.count(0))