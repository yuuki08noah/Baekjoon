import sys
import math
from bisect import bisect_left

def hanoi(n, start, end, temp):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, temp, end)
        print(start, end)
        hanoi(n-1, temp, end, start)
input = sys.stdin.readline
n = int(input())
print(pow(2, n)-1)
if n <= 20:
    hanoi(n, 1, 3, 2)