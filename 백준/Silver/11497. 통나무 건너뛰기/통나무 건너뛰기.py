import decimal
import sys
import math
import heapq

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    temp = []
    for i in range(len(arr)):
        # print(temp)
        if i % 2 == 0:
            temp.insert(i//2, arr[i])
        elif i == 1:
            temp.append(arr[i])
        else:
            temp.insert(-i//2+1, arr[i])
    # print(temp)
    max = 0
    for i in range(len(temp)):
        if max < abs(temp[i-1]-temp[i]):
            max = abs(temp[i-1]-temp[i])
    print(max)